# app/models.py
import os
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import pandas as pd

# Load BM25 and SBERT models
class ModelLoader:
    def __init__(self, data_path: str):
        # Load data and tokenize for BM25
        self.data_chunks = pd.read_csv(data_path)
        self.bm25 = BM25Okapi([doc.split(" ") for doc in self.data_chunks['text'].values])
        self.sbert_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    def get_bm25(self):
        return self.bm25

    def get_sbert_model(self):
        return self.sbert_model

    def get_data_chunks(self):
        return self.data_chunks
