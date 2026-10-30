from typing import List,Dict,TypedDict
from pydantic import BaseModel,Field

class SensorAnomalyItem(BaseModel):
    anomaly_pair:Dict[str,bool]=Field("Key:sensor id,value:boolean is empty or not!")

class SensorAnomaly(BaseModel):
    anomaly_report:str=Field(description="Summary of detected sensor anomalies!")
    anomalies:List[SensorAnomalyItem]=Field(description="List of anomaly assesments")

class Recommendation(BaseModel):
    recommendation:str=Field(description="Practical recommendation to the farmer based on the farm data ")
    anomaly_suspected:bool=Field(description="Do you suspect that there is anomaly!")

class FarmerState(TypedDict):
    topic:str|None 
    plots:List[Dict]|None 
    sensor_readings:List[Dict]|None 
    recommendation:str|None
    anomaly_suspected:bool 
    anomaly_report:str|None 
    anomalies:List[SensorAnomalyItem]
    



