from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
while True:
    user_input = input("You :")
    
    if user_input.lower() == "exit":
        break
    
    result = model.invoke(user_input)
    print("Bot :", result.content)
    
    
    