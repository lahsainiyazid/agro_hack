from src.utils.nodes import create_recommendation,detect_sensor_anomalies,sensor_anomaly_router
from langgraph.graph import START,END,StateGraph
from typing import List,Tuple 
from src.utils.objects import FarmerState 
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())

#We create here our graph object
builder=StateGraph(FarmerState)
#Here we have our nodes:
builder.add_node("create_recommendation",create_recommendation)
builder.add_node("detect_sensor_anomalies",detect_sensor_anomalies)
#Here we add our edges:
builder.add_edge(START,"create_recommendation")
builder.add_conditional_edges("create_recommendation",sensor_anomaly_router)
builder.add_edge("detect_sensor_anomalies",END)

graph=builder.compile()
