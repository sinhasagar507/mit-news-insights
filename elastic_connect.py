import os
from elasticsearch import Elasticsearch, exceptions
from langchain_elasticsearch import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings
import streamlit as st
from session_keys import ensure_keys_in_session

# All the required environment variables 
ELASTIC_INDEX_NAME = "openai_mit_llama_index"

def retrieve_vector_store():
   
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