from pydantic import BaseModel,Field
from typing import List,Tuple

class FarmerState(BaseModel):
    topic:str|None=Field(description="Farmer question")
    plots:List[Tuple]=Field(description="List of our plots readings") 
    sensor_readings:List[Tuple]=Field(description="List of sensor readings from the field!")
    analysis:str=Field(description="Analysis and thought process of our ai agent!")
    recommandation:str=Field(description="Recommandation given by our ai agent!") 


