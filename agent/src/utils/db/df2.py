import pandas as pd
from pathlib import Path 
from src.utils.db.db_path2 import db_path 
from src.utils.db.get_sensors2 import get_last_h_readings 
from typing import List,Dict



def print_df(path:Path=db_path):
    df=pd.DataFrame(get_last_h_readings(db_path))
    print(df)
def check_anomaly(path:Path=db_path)->List[Dict[str,bool]]:
    df=pd.DataFrame(get_last_h_readings(db_path))
    df["soil_moisture_anom"]=((df["soil_moisture"]<0)|(df["soil_moisture"]>100))
    df["air_temp_anom"]=((df["air_temperature"]>55) | (df["air_temperature"]<-5))
    df["air_hum_anom"]=((df["air_humidity"]<0)|(df["air_humidity"]>100))
    df["soil_temperature_anom"]=((df["soil_temperature"]<0)|(df["soil_temperature"]>50))
    df["rainfall_anom"]=((df["rainfall_mm"]<0)|(df["rainfall_mm"]>100))
    anomaly_cols=["soil_moisture_anom","air_temp_anom","air_hum_anom","soil_temperature_anom","rainfall_anom"]
    df_anom=df[anomaly_cols].any(axis=1)
    anom_list=[{str(idx):val} for idx,val in df_anom.items()]
    return anom_list
if __name__=="__main__":
   

