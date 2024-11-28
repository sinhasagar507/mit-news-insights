import os
import streamlit as st

# Shared function to ensure keys are in session_state
def ensure_keys_in_session():
    """Ensure required keys are initialized in st.session_state."""
    if "chatbot_api_key" not in st.session_state or not st.session_state["chatbot_api_key"]:
        st.session_state["chatbot_api_key"] = "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"
        
    os.environ["OPENAI_API_KEY"] = "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"

    if "elastic_database_id" not in st.session_state or not st.session_state["elastic_database_id"]:
        st.session_state["elastic_database_id"] = "d044420c15ae4d46ba038431ea25fb43:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDA1MjRmZGEyNGQ3OTQ0MWJiN2IyMTAxY2FkMzQ0MDc4JDhkNzY1MTE5YWM5ZjQ1ZjZiNjNhNjczYWUxZmRjNGZi"

    if "elastic_api_key" not in st.session_state or not st.session_state["elastic_api_key"]:
        st.session_state["elastic_api_key"] = "NDJoZGJwTUJjZ2JpUWQ0aTVrZWo6Qlhra1VlbnVTQW1tTGN2REZBeG8zdw=="