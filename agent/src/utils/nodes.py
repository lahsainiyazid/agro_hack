from dotenv import load_dotenv,find_dotenv 
from src.utils.objects import FarmerState,Recommendation 
from src.utils.models import llm  
from src.utils.prompts import prompt
from src.utils.db.get_sensors import get_last_24h_readings
from src.utils.db.get_plots import get_all_plots
from src.utils.db.db_path import db_path 
from langchain.messages import SystemMessage,HumanMessage



def create_recommendation(state:FarmerState):
    """
    Creating our farmer!
    """
    topic=state.get("topic","")
    plots=get_all_plots(db_path)
    sensor_readings=get_last_24h_readings(db_path)
    structured_llm=llm.with_structured_output(Recommendation)
    system_message=prompt.format(sensor_readings=sensor_readings,
                                 plots=plots)
    recom=structured_llm.invoke([SystemMessage(content=system_message),HumanMessage(content="Generate the best possible recommendation to our farm")])
    return {"recommendation":recom.recommendation}
    

