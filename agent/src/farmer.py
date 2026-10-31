from src.utils.nodes2 import detect_manual_sensor_anomalies,sensor_anomaly_router,send_alert,write_alert_router,fetch_farm_data,test_recommendation,write_recommendation,write_alert,take_action
from langgraph.graph import START,END,StateGraph
from typing import List,Tuple 
from src.utils.objects2 import FarmerState 
from dotenv import load_dotenv,find_dotenv 
_=load_dotenv(find_dotenv())

#We create here our graph object
builder=StateGraph(FarmerState)
#Here we have our nodes:
builder.add_node("fetch_data",fetch_farm_data)
builder.add_node("detect_anomalies",detect_manual_sensor_anomalies)
builder.add_node("create_recommendation",test_recommendation)
builder.add_node("write_recommendation",write_recommendation)
builder.add_node("take_action",take_action)
builder.add_node("write_alert",write_alert)
builder.add_node("send_alert",send_alert)
#Here we add our edges:
builder.add_edge(START,"fetch_data")
builder.add_edge("fetch_data","detect_anomalies")
builder.add_edge("detect_anomalies","create_recommendation")
builder.add_edge("create_recommendation","write_recommendation")
builder.add_edge("write_recommendation","take_action")
builder.add_conditional_edges("take_action",write_alert_router)
builder.add_edge("write_alert","send_alert")
builder.add_edge("send_alert",END)

graph=builder.compile()
