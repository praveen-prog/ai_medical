from langchain_core.tools import tool
from utils.euri_client import euri_chat_completion

@tool
def ai_diagnosis(symptom_description):
    """ Check the diganosis based on the description provided"""

    message = [
        {
            "role" : "user",
            "content" : f"based on the symptom {symptom_description} give diagnosis and treatment as applicable"    
        }
    ]


    return euri_chat_completion(messages=message)


