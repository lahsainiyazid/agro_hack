from src.utils.nodes import create_recommendation
from langgraph.graph import START,END,StateGraph
from src.utils.objects import FarmerState 
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
builder=StateGraph(FarmerState)
builder.add_node("create_farmer",create_recommendation)
builder.add_edge(START,"create_farmer")
builder.add_edge("create_farmer",END)
graph=builder.compile()
