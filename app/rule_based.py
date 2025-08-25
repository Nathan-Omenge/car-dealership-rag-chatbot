# app/rule_based.py

def rule_based_response(query, context):
    if "hours" in query.lower():
        return "Our dealership is open from 8am to 6pm Monday through Saturday."
    if "location" in query.lower():
        return "We are located in Westlands, next to Sarit Centre."
    return "I'm sorry, I couldn't find an exact answer. Please try rephrasing."
