import os 
import requests 
from dotenv import load_dotenv,find_dotenv 
from src.utils.objects2 import FarmerState,Recommendation,SensorAnomaly 
from src.utils.models2 import llm,local_llm 
from src.utils.prompts2 import recom_prompt,anomaly_prompt
from src.utils.db.get_sensors2 import get_last_24h_readings
from src.utils.db.get_plots2 import get_all_plots
from src.utils.db.db_path2 import db_path 
from langchain.messages import SystemMessage,HumanMessage
from langgraph.graph import END

_=load_dotenv(find_dotenv())
TOKEN=os.environ.get("BOT_TOKEN")
CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
def create_recommendation(state:FarmerState):
    """
    Creating our recommendation!
    """
    topic=state.get("topic","")
    plots=get_all_plots(db_path)
    sensor_readings=get_last_24h_readings(db_path)
    structured_llm=local_llm.with_structured_output(Recommendation)
    system_message=recom_prompt.format(sensor_readings=sensor_readings,
                                 plots=plots)
    recom=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="Generate the best possible recommendation to our farm")])
    return {
        "plots":plots ,
        "sensor_readings":sensor_readings,
            "recommendation":recom.recommendation,
        "anomaly_suspected":recom.anomaly_suspected}
    
def detect_sensor_anomalies(state:FarmerState):
    """
    Here we already have a state after the first node so no need to pass our state 
    """
    sensor_readings=state.get("sensor_readings","")
    plots=state.get("plots","")
    recommendation=state.get("recommendation","")
    anomaly_suspected=state.get("anomaly_suspected")
    structured_llm=local_llm.with_structured_output(SensorAnomaly)
    system_message=anomaly_prompt.format(
        sensor_readings=sensor_readings,
        plots=plots,
        recommendation=recommendation,
        anomaly_suspected=anomaly_suspected
    )
    anomaly=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="Check if there is an anomaly or not!")])
    return {
    "anomaly_report":anomaly.anomaly_report,
     "anomalies":anomaly.anomalies
    }

def sensor_anomaly_router(state:FarmerState):
    """
    Here i make a small router function that checks if the llm has decided if there is an anomly or not !
    """
    if (state.get("anomaly_suspected")):
        return "detect_sensor_anomalies"
    return END

def send_alert(state:FarmerState):

    """
    Here is a small python function to send alert if there is an anomaly 
    """
    anomaly_report=str(state.get("anomaly_report"))
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
    "chat_id": CHAT_ID,
    "text": anomaly_report}
    requests.post(url,json=payload)

def send_alert_router(state:FarmerState):
    """
    Here is a simple anomlay router script to send alerts
    """
    if (state.get("anomaly_suspected")):
        return "send_alert"
    return END

    
