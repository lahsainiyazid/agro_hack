from dotenv import load_dotenv,find_dotenv 
from utils.states import FarmerState 
from utils.models import llm 
from utils.objects import Farmer 
from utils.prompts import prompt
from db.get_sensors import get_last24h_readings
from db.get_plots import get_all_plots
from db.db_path import db_path 
from langchain.messages import SystemMessage,HumanMessage



def create_recommendation(state:FarmerState):
    """
    Creating our farmer!
    """
    topic=state.get("topic","")
    human_feedback=state.get("human_feedback","")
    plots=get_all_plots(db_path)
    sensor_readings=get_last24h_readings(db_path)
    structured_llm=llm.with_structured_output(Farmer)
    system_message=prompt.format(sensor_readings=sensor_readings,
                                 plots=plots)
    recommendation=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="Generate the best possible recommendation to our farm")])
    return {"recommendation":recommendation.recommendation}
    

