from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
st.header("Chatbot")
st.caption("This chatbot is powered by LLaMA 3.3 70B Versatile model from Groq. It is designed to provide helpful responses in a concise manner. If the model doesn't know the answer, it will respond with 'I don't know'.")
#create a session state to store the chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant. Always answer in a 4-5 sentence format. If you don't know the answer, say 'I don't know'.")]
    
# Display the previous chat messages

for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    
    with st.chat_message(role):
        st.write(message.content)
        
with st.sidebar:
    st.subheader("Chat History")
    if not st.session_state.chat_history:
        st.write("No chat history yet.")
    else:
        for msg in st.session_state.chat_history:
            role = "User" if isinstance(msg, HumanMessage) else "AI"
            st.write(f"**{role}:** {msg.content}")
        
        
# Get user input
user_input = st.chat_input("Type your message here...")

if user_input:
    if user_input.strip().lower() == "exit":
        st.stop()
    
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )
    
    with st.chat_message("user"):
        st.write(user_input)
        
    result = model.invoke(st.session_state.chat_history)
    
    st.session_state.chat_history.append(
        AIMessage(content=result.content)
    )
    
    with st.chat_message("assistant"):
        st.write(result.content)
        

