# app/rerank.py
from sentence_transformers import util

def rerank_chunks(query, chunks, sbert_model):
    similarities = []
    for _, chunk in chunks.iterrows():
        embedding = sbert_model.encode([query, chunk['text']])
        similarity = util.pytorch_cos_sim(embedding[0], embedding[1])
        similarities.append(similarity.item())
    
    chunks['similarity'] = similarities
    return chunks.nlargest(3, 'similarity')
