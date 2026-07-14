from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)
# llm = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )

# result = llm.invoke("What is the capital of Bangladesh?")
result = llm.invoke("Write a pome on love in 4 lines.")

print(result.content)