import os
import streamlit as st

# Shared function to ensure keys are in session_state
def ensure_keys_in_session():
    """Ensure required keys are initialized in st.session_state."""
    if "chatbot_api_key" not in st.session_state or not st.session_state["chatbot_api_key"]:
        st.session_state["chatbot_api_key"] = os.environ["OPENAI_API_KEY"]

    if "elastic_database_id" not in st.session_state or not st.session_state["elastic_database_id"]:
        st.session_state["elastic_database_id"] = os.environ["ELASTIC_CLOUD_ID"]

    if "elastic_api_key" not in st.session_state or not st.session_state["elastic_api_key"]:
        st.session_state["elastic_api_key"] = os.environ["ELASTIC_API_KEY"]

    # Set environment variable for OpenAI
    # os.environ["OPENAI_API_KEY"] = st.session_state["chatbot_api_key"]