# tests/test_pipeline.py
from app.intent_classifier import classify_intent
from app.rule_based import rule_based_response

# Test 1: Intent Classification
def test_classify_price_query():
    assert classify_intent("How much does a Honda cost?") == "price_query"

def test_classify_vehicle_info():
    assert classify_intent("Tell me about Toyota models from 2022") == "vehicle_info"

def test_classify_business_info():
    assert classify_intent("Where is your dealership located?") == "business_info"

def test_classify_general():
    assert classify_intent("Do you have recommendations?") == "general_query"

# Test 2: Rule-based fallback

def test_rule_response_hours():
    response = rule_based_response("What are your business hours?", "")
    assert "open from" in response

def test_rule_response_location():
    response = rule_based_response("Where are you located?", "")
    assert "located at" in response

def test_rule_response_unknown():
    response = rule_based_response("What deals do you have?", "")
    assert "couldn't find" in response
