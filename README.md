# Enhanced RAG-Based Chatbot for Car Dealerships

A production-ready Retrieval-Augmented Generation (RAG) chatbot built to automate customer support in automotive dealerships. This system integrates semantic search, multi-intent classification, and a multi-LLM fallback response pipeline to answer complex customer queries.

---

##  Project Summary

This chatbot is designed to solve common customer service challenges in car dealerships:

-  Manual search through large vehicle inventories
-  Inconsistent service quality
-  Limited human availability
-  Inability to handle complex or multi-attribute queries

 My system provides a scalable, intelligent assistant that can:
- Retrieve vehicle details (e.g., fuel, price, transmission)
- Respond to dealership-related questions (location, hours, services)
- Automate responses using a smart fallback strategy (LLM + rule-based)

---

##  Architecture Overview

```
User Query
   ↓
Intent Classifier
   ↓
Retriever (ChromaDB + SentenceTransformer)
   ↓
Generator:
   ├── Primary: Phi-2
   ├── Fallback: GPT-2
   └── Rule-based response
   ↓
Chatbot Response
```

---

##  Repository Structure

```
car-dealership-rag-chatbot/
├── README.md
├── requirements.txt
├── poster.pdf
│
├── notebook/
│   └── Enhanced_Car_Dealership_RAG_Model.ipynb
│
├── app/
│   ├── main.py                  # Orchestrates user interaction
│   ├── retriever.py             # Vector store + semantic search
│   ├── generator.py             # Multi-LLM response pipeline
│   ├── intent_classifier.py     # Regex-based intent routing
│   └── rule_based.py            # Hardcoded response fallback
│
├── data/
│   ├── dealership_inventory.csv # Sample dataset (car metadata)
│   ├── business_info.json       # Store info (location, hours, contact)
│   └── customer_questions.csv   # Realistic labeled query examples
│
├── models/                      # Optional: saved vector stores
│
└── tests/
    └── test_pipeline.py         # Unit tests for classifier + fallback
```

---

##  How to Run the Chatbot Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/car-dealership-rag-chatbot.git
cd car-dealership-rag-chatbot
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot in Terminal
```bash
cd app
python main.py
```
You'll be prompted to enter a question like:
```
User: What time do you close?
Bot: Our dealership is open from 8am to 6pm Monday through Saturday.
```

### 5. Run Tests (Optional)
```bash
pytest tests/
```

---

## 🔍 Examples of Customer Queries
Examples from `data/customer_questions.csv` include:
- "What’s the fuel consumption of this car?" → `vehicle_info`
- "Where is your dealership located?" → `business_info`
- "Does this car come in automatic transmission?" → `vehicle_info`
- "Are you open on weekends?" → `business_info`

These are used to benchmark and test your chatbot’s coverage.

---

##  Results Summary

| Metric                      | Before     | After (RAG Pipeline) | Change |
|----------------------------|------------|------------------------|--------|
| Retrieval Precision@10     | 0.76       | 0.92                   | +21%   |
| Intent Classification Acc. | 0.82       | 0.95                   | +16%   |
| Response Latency (ms)      | 2100       | 847                    | -60%   |
| Memory Usage (GB)          | 8.1        | 3.2                    | -60%   |

---

##  Dependencies
```
transformers
sentence-transformers
chromadb
torch
pandas
scikit-learn
pytest
```
You can generate this via `pip freeze > requirements.txt`.

---

##  Poster Summary
See `poster.pdf` for a one-page summary of the RAG architecture, dataset pipeline, evaluation metrics, and key insights.

---

##  Authors
- Nathan Orang'o Omenge
- Collins Gitau
- Leona Kamau
- Mark Mayana

United States International University – Africa

---

##  License
This project is licensed under the MIT License.

---

##  Future Work
- Integrate real-time vehicle inventory APIs
- Expand multilingual support
- Add Streamlit or web UI for demo deployment

---

##  Need Help?
Open an issue or reach out via GitHub if you'd like help deploying this chatbot in your own dealership, business, or research environment.

---
