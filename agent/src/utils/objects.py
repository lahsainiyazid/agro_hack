from pydantic import BaseModel,Field


class Farmer(BaseModel):
    plot_id:int
    plot_data:dict 
    sensor_readings=list[str]
    analysis:str 
    recommandation:str 


