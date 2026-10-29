from typing import TypedDict,List,Tuple,Optional 
from pydantic import BaseModel,Field 
class FarmerState(TypedDict):
    topic:str|None 
    plots:List[Tuple]|None 
    sensor_readings:List[Tuple]|None 
    recommendation:str|None 
     
class Recommendation(BaseModel):
    recommendation:str=Field(description="Practical recommendation to the farmer based on the farm data ")


