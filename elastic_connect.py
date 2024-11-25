# import os
# from getpass import getpass
# from elasticsearch import Elasticsearch, exceptions
# from langchain_elasticsearch import ElasticsearchStore
# from langchain_core.prompts import MessagesPlaceholder
# from langchain.embeddings.openai import OpenAIEmbeddings
# import streamlit as st

# # All the required environment variables 
# ELASTIC_INDEX_NAME = "openai_mit_llama_index"


# OPENAI_API_KEY = st.session_state["chatbot_api_key"]
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# ELASTIC_CLOUD_ID = st.sidebar.text_input("Elastic Cloud ID", key="elastic_database_id", type="password")
# ELASTIC_API_KEY = st.sidebar.text_input("Elastic API key", key="elastic_api_key", type="password")


# def retrieve_vector_store():
#     embeddings = OpenAIEmbeddings()
#     vector_store = ElasticsearchStore(
#         es_cloud_id=ELASTIC_CLOUD_ID,
#         es_api_key=ELASTIC_API_KEY,
#         index_name=ELASTIC_INDEX_NAME,
#         embedding=embeddings,
#     )
    
#     return vector_store

import os
from elasticsearch import Elasticsearch, exceptions
from langchain_elasticsearch import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings
import streamlit as st
from session_keys import ensure_keys_in_session

# All the required environment variables 
ELASTIC_INDEX_NAME = "openai_mit_llama_index"

def retrieve_vector_store():
    # # Check if the required session state variables are set
    # if not all(
    #     key in st.session_state and st.session_state[key]
    #     for key in ["chatbot_api_key", "elastic_database_id", "elastic_api_key"]
    # ):
    #     # Return None silently if any variable is missing
    #     return None

    # Retrieve values from session state
    # if "elastic_database_id" not in st.session_state:
    #     st.session_state["elastic_database_id"] = "ab9fc665e06642b4b2c99c5f9898e875:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDg3MzIwMzg0YWMzNzRjNTJiYmQ3YWFkYjI4NWUxNjExJDIxMDFiZTgzNjg5ODQ0MmFhMzg4ZTMzYzU5MTdmOTlh"
        
    # if "elastic_api_key" not in st.session_state:
    #     st.session_state["elastic_api_key"] = "WUoyVkpKTUJ0ZTlkVlhESWtSVDQ6eGUwY1dzcmlSbGE4bW5iY2gxQl9CZw=="
        
    # if "chatbot_api_key" not in st.session_state:
    #     st.session_state["chatbot_api_key"] = "sk-JDd8XASldxnf4JlfzqcFX6IZkRp88UQSOuS6MqsBgLT3BlbkFJoaFWr04LuZoWZQlTBdTzxzbQ7tgFTD2iXbICVfLxcA"
        
    # os.environ["OPENAI_API_KEY"] = st.session_state["chatbot_api_key"]
    ensure_keys_in_session()

    # Initialize the ElasticsearchStore
    embeddings = OpenAIEmbeddings()
    vector_store = ElasticsearchStore(
        es_cloud_id=st.session_state["elastic_database_id"],
        es_api_key=st.session_state["elastic_api_key"],
        index_name=ELASTIC_INDEX_NAME,
        embedding=embeddings,
    )
    
    return vector_store