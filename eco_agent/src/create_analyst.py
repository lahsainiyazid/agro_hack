from langgraph.graph import START,END,StateGraph
from src.utils.objects import analyst
from src.utils.nodes import fetch_data_bourse_agro


builder=StateGraph(analyst)
builder.add_node("fetch_data_1",fetch_data_bourse_agro)
builder.add_edge(START,"fetch_data_1")
builder.add_edge("fetch_data_1",END)
graph=builder.compile()

