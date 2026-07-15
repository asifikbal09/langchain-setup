from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

document=[
    "I love AI",
    "I love LangChain",
    "I love Python"
]


vectors = embeddings.embed_documents(document)

print(len(vectors), len(vectors[0]), vectors[0][:10])