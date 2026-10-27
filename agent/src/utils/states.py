from typing_extensions import TypedDict 
from typing import NotRequired,Optional
from objects import Farmer

class Farmer(TypedDict):
    question:str
    human_feedback:NotRequired[str]
    farmers:NotRequired[List[Farmer]]

