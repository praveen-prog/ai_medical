from langchain.tools import tool



def categorize_symptom(symptom):
    # Define symptom categories with associated keywords
    categories = {
        "infection": ["fever", "body ache", "chills"],
        "respiratory": ["throat", "cough"],
        "migraine": ["headache", "dizzy"],
        "gastro": ["stomach", "nausea"]
    }

    # Convert symptom to lowercase for case-insensitive matching
    symptom_lower = symptom.lower()

    # Check each category
    for category, keywords in categories.items():
        if any(keyword in symptom_lower for keyword in keywords):
            return category

    # Default category if no match found
    return "general exam"

@tool
def check_symptom(symptom):
    """ Analyse the sympton and provide treatment"""
    return categorize_symptom(symptom)     