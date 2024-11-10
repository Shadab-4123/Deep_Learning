# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import ModelLoader
from app.retrieve import get_top_n_chunks
from app.rerank import rerank_chunks
from app.generate import generate_answer
import os

# Load models and data
model_loader = ModelLoader(data_path="data_chunks.csv")
bm25 = model_loader.get_bm25()
sbert_model = model_loader.get_sbert_model()
data_chunks = model_loader.get_data_chunks()

# Configure FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/query", response_class=HTMLResponse)
async def post_query(request: Request, query: str = Form(...)):
    # Step 1: Retrieve top chunks using BM25
    top_chunks = get_top_n_chunks(query, bm25, data_chunks, n=10)
    
    # Step 2: Rerank top chunks using SBERT
    reranked_chunks = rerank_chunks(query, top_chunks, sbert_model)
    
    # Step 3: Generate answer using Gemini
    answer = generate_answer(query, reranked_chunks)
    
    return templates.TemplateResponse("index.html", {"request": request, "query": query, "answer": answer})
