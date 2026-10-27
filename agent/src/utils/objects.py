from pydantic import BaseModel,Field


class Farmer(BaseModel):
    region:str=Field(description="Describe the moroccan region the farmer is from !")
    name:str=Field(description="Name of our farmer")
    role:str=Field(description="Role of our farmer in the context of the topic")
    description:str=Field(description="Description of the farmer his roles and motives!")
    @property
    def persona(self)->str:
        return f"name:{self.name}\nregion:{self.region}\nrole{self.role}\ndescription{self.description}"

