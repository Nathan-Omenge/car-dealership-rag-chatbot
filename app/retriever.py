# app/retriever.py
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.get_or_create_collection("car_inventory")

def retrieve_documents(query, top_k=5):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["documents"][0]