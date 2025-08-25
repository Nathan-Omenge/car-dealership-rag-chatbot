# app/main.py
from retriever import retrieve_documents
from intent_classifier import classify_intent
from generator import generate_response

def handle_user_query(query):
    intent = classify_intent(query)
    docs = retrieve_documents(query, top_k=5)
    response = generate_response(query, docs, intent)
    return response

if __name__ == "__main__":
    print("Welcome to the Car Dealership RAG Chatbot!")
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        reply = handle_user_query(user_input)
        print(f"Bot: {reply}")
