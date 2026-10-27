from typing_extensions import TypedDict 
from typing import NotRequired,Optional
from objects import Farmer

class GenerateFarmerState(TypedDict):
    topic:str
    human_feedback:NotRequired[str]
    farmer:Farmer

