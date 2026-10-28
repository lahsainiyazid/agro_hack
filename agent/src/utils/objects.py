from pydantic import BaseModel,Field
from typing import List,Dict 

class Farmer(BaseModel):
    plot_id:int=Field(description="Ids of our plots")
    plot_data:Dict[str,str]=Field(description="Data of our plots")
    sensor_readings:List[str]=Field(description="List of sensor readings from the field!")
    analysis:str=Field(description="Analysis and thought process of our ai agent!")
    recommandation:str=Field(description="Recommandation given by our ai agent!") 


