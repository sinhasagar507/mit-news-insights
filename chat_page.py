import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from rag_setup import rag
from session_keys import ensure_keys_in_session
from utils import clear_chat_history

def clear_chat_history():
    """Clears the chat history from the session state."""
    if "chat_history" in st.session_state:
        del st.session_state["chat_history"]

def chat():
    with st.sidebar:
        st.slider("Response Creativity (Temperature)", 0.0, 1.0, 0.5, key="temperature")
        st.slider("Max Tokens", 50, 500, 150, key="tokens")
        
        if st.sidebar.button("Clear Chat"):
            clear_chat_history()
            
    ensure_keys_in_session()
    
    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = [{"role": "assistant", "content": "How can I help you?"}]
        
    # Print all the initial messages in the existing session state
    for message in st.session_state["chat_history"]:
        st.chat_message(message["role"]).write(message["content"])
        
    if prompt := st.chat_input():
        openai_api_key = st.session_state["chatbot_api_key"]
        elastic_database_id = st.session_state["elastic_database_id"]
        elastic_api_key = st.session_state["elastic_api_key"]
        
        if not openai_api_key or not elastic_database_id or not elastic_api_key:
            st.info("Please add all your IDs and API keys to continue.")
            st.stop()
            
        st.session_state["chat_history"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        rag_chain = rag()
        response = rag_chain.invoke({"input": prompt, "chat_history": st.session_state["chat_history"]})
        message = response["answer"]
        st.session_state["chat_history"].append({"role": "assistant", "content": message})
        st.chat_message("assistant").write(message)
            
    

    
        
    
            

        
    

    
    
