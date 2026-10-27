from utils.nodes import create_farmer
from langgraph.graph import START,END,StateGraph
from utils.states import GenerateFarmerState
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
builder=StateGraph(GenerateFarmerState)
builder.add_node("create_farmer",create_farmer)
builder.add_edge(START,"create_farmer")
builder.add_edge("create_farmer",END)
graph=builder.compile()
