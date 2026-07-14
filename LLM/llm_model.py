# Old fashioned way of using Google Gemini API with LangChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

result = llm.invoke("What is the capital of Bangladesh?")

print(result)