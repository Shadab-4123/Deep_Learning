# app/generate.py
import google.generativeai as genai

def generate_answer(query, selected_chunks):
    combined_text = " ".join(selected_chunks['text'].values)
    prompt = (
        f"Query: {query}\n\n"
        f"Based on the following information, please provide a concise and informative answer:\n\n"
        f"{combined_text}\n\n"
        "Answer:"
    )
    response = genai.generate_content(prompt)
    return response.text
