from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

chat_history = [SystemMessage(content="You are a helpful assistant. Always answer in a 2-3 sentence format. If you don't know the answer, say 'I don't know'.")]

while True:
    user_input = input("You :")
    # chat_history.append({"role": "user", "content": user_input})
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        break
    
    result = model.invoke(chat_history)
    # chat_history.append({"role": "assistant", "content": result.content})
    chat_history.append(AIMessage(content=result.content))
    print("Bot :", result.content)
    
    
    