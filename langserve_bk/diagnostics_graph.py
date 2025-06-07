from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from tools.diagnosis_tool import ai_diagnosis
from tools.symptoms_checker import check_symptom

class DiagnosisState(TypedDict):
    input : str
    symptom_area : str
    diganosis : str

def build_graph():
    graph = StateGraph(DiagnosisState)    
    
    def symptom_step(state):
        return {
                "input" : state["input"],
                "symptom_area" : check_symptom.invoke(state["input"]),
                "diganosis" : state.get("diagnosis")
        }


    graph.add_node("symptom_check",RunnableLambda(symptom_step))


    def diagnosis_step(state):
        return {
                "input" : state["input"],
                "symptom_area" : state['symptom_area'],
                "diganosis" : ai_diagnosis.invoke(state['input'])
        }


    graph.add_node("diganosis_check",RunnableLambda(diagnosis_step))

    graph.set_entry_point("symptom_check")
    graph.add_edge("symptom_check","diganosis_check")
    graph.add_edge("diganosis_check",END)

    return graph.compile()

    