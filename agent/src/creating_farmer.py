from src.utils.nodes import create_recommendation
from langgraph.graph import START,END,StateGraph
from typing import List,Tuple 
from src.utils.objects import FarmerState 
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())
builder=StateGraph(FarmerState)
builder.add_node("create_recommendation",create_recommendation)
builder.add_edge(START,"create_recommendation")
builder.add_edge("create_recommendation",END)
graph=builder.compile()
