from pydantic import BaseModel,Field
from typing import List 

class FarmerState(BaseModel):
    plots:List[Tuple]=Filed(description="List of our plots readings") 
    sensor_readings:List[Tuple]=Field(description="List of sensor readings from the field!")
    analysis:str=Field(description="Analysis and thought process of our ai agent!")
    recommandation:str=Field(description="Recommandation given by our ai agent!") 


