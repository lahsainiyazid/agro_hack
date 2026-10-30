from typing import TypedDict,List,Tuple,Optional 
from pydantic import BaseModel,Field 
class FarmerState(TypedDict):
    topic:str|None 
    plots:List[Tuple]|None 
    sensor_readings:List[Tuple]|None 
    recommendation:str|None
    anomaly_suspected:bool 
    anomaly_report:str|None 
    anomalies:List[SensorAnomalyItem]
class Recommendation(BaseModel):
    recommendation:str=Field(description="Practical recommendation to the farmer based on the farm data ")
    anomaly_suspected:bool=Field(description="Do you suspect that there is anomaly!")

class SensorAnomaly(BaseModel):
    anomaly_report:str=Field(description="Summary of detected sensor anomalies!")
    anomalies:List[SensorAnomalyItem]=Field(description="Anomaly assesment for each sensor reading")
    
class SensorAnomalyItem(BaseModel):
    sensor_id:str=Field(description="Id of the sensor")
    is_anomaly:bool=Field(description="Is it anomaly or not ")
    explanation:str=Field(description="Reasoning behind why it is anomaly or not!")


