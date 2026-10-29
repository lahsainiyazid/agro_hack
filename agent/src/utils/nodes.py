from dotenv import load_dotenv,find_dotenv 
from src.utils.objects import FarmerState,Recommendation 
from src.utils.models import llm  
from src.utils.prompts import recom_prompt,anomaly_prompt
from src.utils.db.get_sensors import get_last_24h_readings
from src.utils.db.get_plots import get_all_plots
from src.utils.db.db_path import db_path 
from langchain.messages import SystemMessage,HumanMessage
from langgraph.graph import END


def create_recommendation(state:FarmerState):
    """
    Creating our recommendation!
    """
    topic=state.get("topic","")
    plots=get_all_plots(db_path)
    sensor_readings=get_last_24h_readings(db_path)
    structured_llm=llm.with_structured_output(Recommendation)
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
    structured_llm=llm.with_structured_output(SensorAnomaly)
    systsem_prompt=llm.with_structured_output(
        sensor_readings=sensor_readings,
        plots=plots,
        recommendation=recommendation,
        anomaly_suspected=anomaly_suspected
    )
    anomaly=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="Check if there is an anomaly or not!")])
    return {
    "anomaly_report":anomaly.anonmaly_report,
     "is_real_anomaly":anomaly.is_real_annomaly
    }

def sensor_anomaly_router(state:FarmerState):
    """
    Here i make a small router function that checks if the llm has decided if there is an anomly or not !
    """
    if (state.get("anomaly_suspected")):
        return "detect_sensor_anomalies"
    return END
