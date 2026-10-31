from pydantic import BaseModel,Field 
from typing import List,Dict,Optional
class analyst(BaseModel):
    agro_bourse_data:Optional[List[Dict[str,str]]]=Field(description="List of dictionnaries name:price",default_factory=list)
