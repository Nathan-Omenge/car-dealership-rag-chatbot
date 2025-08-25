# app/intent_classifier.py
import re

def classify_intent(query):
    query = query.lower()
    if re.search(r'price|cost|budget', query):
        return "price_query"
    elif re.search(r'make|model|brand|year', query):
        return "vehicle_info"
    elif re.search(r'hours|location|service|contact', query):
        return "business_info"
    else:
        return "general_query"
