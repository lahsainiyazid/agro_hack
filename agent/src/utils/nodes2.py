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
     Sensor_anomalies:{state["anomalies"]}
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
    anom_list=[{str(idx+1):val} for idx,val in df_anom.items()]
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

def write_alert_router(state:FarmerState):
    """
    Here is a simple anomaly  router script to send alerts
    """
    if (state.get("anomaly_suspected")):
        return "write_alert"
    return END

def write_recommendation(state:FarmerState):
    file_path=Path("/home/yazid/agro/agent/src/utils/recommendation.txt")
    file_path.write_text(state["recommendation"])

def write_alert(state:FarmerState):
    file_path=Path("/home/yazid/agro/agent/src/utils/alert.txt")
    file_path.write_text(state["anomaly_report"])
   

def take_action(state:FarmerState):
    plots=state["plots"]
    sensor_readings=state["sensor_readings"]
    anomalies=state["anomalies"]
    df_plots=pd.DataFrame(plots)
    df_sensors=pd.DataFrame(sensor_readings)
    df=df_plots.merge(df_sensors,left_on="id",right_on="plot_id")
    anomalies=state["anomalies"]
    anomalies_dict=anomalies[0].anomaly_pair
    df_anomalies=pd.DataFrame(anomalies_dict.items(),columns=["sensor_id","anomaly_status"])
    df=df.merge(df_anomalies,left_on="id_y",right_on="sensor_id")
    action_cols=["moisture_min_pct","moisture_target_pct","anomaly_status","soil_moisture"]
    df_actions=df.apply(decide_action,axis=1)
    df_actions.index=df_actions.index+1
    
    return {
        "actions":df_actions.to_dict(),
    "anomalies_dict":anomalies_dict
    }

def decide_action(row):
    if(row["anomaly_status"]):
        return "CHECK_SENSOR"
    else :
        if (row["soil_moisture"]<row["moisture_min_pct"]):
            return "WATER"
        else:
            return "WAIT"

