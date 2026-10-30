import os
import pandas as pd
import requests 
from dotenv import load_dotenv,find_dotenv 
from pathlib import Path 
from src.utils.objects2 import FarmerState,Recommendation,SensorAnomaly,SensorAnomalyItem 
from src.utils.models2 import llm,local_llm 
from src.utils.prompts2 import recom_prompt,anomaly_prompt,manual_anomaly_prompt
from src.utils.db.get_sensors2 import get_last_h_readings
from src.utils.db.get_plots2 import get_all_plots
from src.utils.db.db_path2 import db_path 
from langchain.messages import SystemMessage,HumanMessage
from langgraph.graph import END

_=load_dotenv(find_dotenv())
TOKEN=os.environ.get("BOT_TOKEN")
CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
def fetch_farm_data(state:FarmerState):
    plots=get_all_plots(db_path)
    sensor_readings=get_last_h_readings(db_path)
    return {"plots":plots,
        "sensor_readings":sensor_readings
    }
def test_recommendation(state:FarmerState):
    prompt=f"""
     You are an agriculture assistant.Based on the following information provide recommendations to the farmer.
     Plots:{state["plots"]}
     Sensor_readings:{state["sensor_readings"]}
            """
    response=local_llm.invoke(prompt)
    return {
        "recommendation":response.content }
    
def detect_manual_sensor_anomalies(path:Path=db_path):
    df=pd.DataFrame(get_last_h_readings(db_path))
    df["soil_moisture_anom"]=((df["soil_moisture"]<0)|(df["soil_moisture"]>100))
    df["air_temp_anom"]=((df["air_temperature"]>55) | (df["air_temperature"]<-5))
    df["air_hum_anom"]=((df["air_humidity"]<0)|(df["air_humidity"]>100))
    df["soil_temperature_anom"]=((df["soil_temperature"]<0)|(df["soil_temperature"]>50))
    df["rainfall_anom"]=((df["rainfall_mm"]<0)|(df["rainfall_mm"]>100))
    anomaly_cols=["soil_moisture_anom","air_temp_anom","air_hum_anom","soil_temperature_anom","rainfall_anom"]
    df_anom=df[anomaly_cols].any(axis=1)
    has_anom=df_anom.any()
    anom_list=[{str(idx):val} for idx,val in df_anom.items()]
    structured_llm=llm.with_structured_output(SensorAnomaly)
    system_message=manual_anomaly_prompt.format(
     data=df,
        anom_list=anom_list
    )
    anomaly=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="check and explain for each sensor if there is an anomaly")])
    return {
        "anomaly_report":anomaly.anomaly_report, 
    "anomalies":anomaly.anomalies,
    "anomaly_suspected":has_anom
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

    
