from typing import TypedDict,List,Dict,Optional 
from pydantic import BaseModel,Field 
class FarmerState(TypedDict):
    topic:str|None 
    plots:List[Dict]|None 
    sensor_readings:List[Dict]|None 
    recommendation:str|None 
     
class Recommendation(BaseModel):
    recommendation:str=Field(description="Practical recommendation to the farmer based on the farm data ")


