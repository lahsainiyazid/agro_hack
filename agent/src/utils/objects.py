from typing import TypedDict,List,Tuple,Optional 
from pydantic import BaseModel,Field 
class FarmerState(TypedDict):
    topic:str|None 
    plots:List[Tuple]|None 
    sensor_readings:List[Tuple]|None 
    recommendation:str|None
    anomaly_suspected:bool 
    anomaly_report:str|None 
    is_real_anomaly:bool 
class Recommendation(BaseModel):
    recommendation:str=Field(description="Practical recommendation to the farmer based on the farm data ")
    anomaly_suspected:bool=Field(description="Do you suspect that there is anomaly!")

class SensorAnomaly(BaseModel):
    anomaly_report:str=Field(description="Check if there is a sensor anomaly")
    is_real_anomaly:bool=Field(description="If you had to predict is it a real anomaly or not!")
