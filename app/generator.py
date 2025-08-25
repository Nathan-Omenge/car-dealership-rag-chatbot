# app/generator.py
from transformers import AutoModelForCausalLM, AutoTokenizer
from rule_based import rule_based_response

# Load fallback LLMs
phi_tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
phi_model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")

gpt2_tokenizer = AutoTokenizer.from_pretrained("gpt2")
gpt2_model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_response(query, docs, intent):
    context = "\n".join(docs)
    input_text = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

    try:
        inputs = phi_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        outputs = phi_model.generate(inputs, max_length=150)
        return phi_tokenizer.decode(outputs[0], skip_special_tokens=True)
    except:
        try:
            inputs = gpt2_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            outputs = gpt2_model.generate(inputs, max_length=150)
            return gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
        except:
            return rule_based_response(query, context)