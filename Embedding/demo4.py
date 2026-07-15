from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


document = [
    "I love programming in Python, It's my favorite language.",
    "JavaScript is great for building web applications.",
    "Eating pizza with friends on a friday night.",
    "Python is awesome for data science and machine learning.",
    "I enjoy hiking and exploring nature on weekends.",
]


query = "I like Python"

doc_vectors = embedding.embed_documents(document)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector], doc_vectors)

print(scores)

index = np.argmax(scores)

print(index)

score = scores[0][index]

print("query:", query)
print("most similar document:", document[index])
print("similarity score:", score)