from dotenv import load_dotenv,find_dotenv 
from utils.states import GenerateFarmerState 
from utils.models import llm 
from utils.objects import Farmer 
from utils.prompts import prompt 
from langchain.messages import SystemMessage,HumanMessage



def create_farmer(state:GenerateFarmerState):
    """
    Creating our farmer!
    """
    topic=state.get("topic","")
    human_feedback=state.get("human_feedback","")
    structured_llm=llm.with_structured_output(Farmer)
    system_message=prompt.structure(topic=topic,
                                    human_feedback=human_feedback)
    farmer=structured_llm.invoke([SystemMessage(content=system_message)],[HumanMessage(content="Please generate the farmer")])
    return {"farmer":farmer.farmer}

