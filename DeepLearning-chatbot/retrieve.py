# app/retrieve.py
def get_top_n_chunks(query, bm25, data_chunks, n=10):
    tokenized_query = query.split(" ")
    scores = bm25.get_scores(tokenized_query)
    top_n_indices = scores.argsort()[-n:][::-1]
    return data_chunks.iloc[top_n_indices]
