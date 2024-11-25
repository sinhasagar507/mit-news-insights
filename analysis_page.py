# from elasticsearch import Elasticsearch

# def analysis():
#     """
#     Data Analysis feature
#     """
#     # First load and show the dataset 
    
#     # Connect to elasticsearch client 
import os
    
#     # Initialize Elasticsearch client
#     es = Elasticsearch(
#         cloud_id=ELASTIC_CLOUD_ID,
#         basic_auth=("elastic", ELASTIC_PASSWORD)
#     )  
    
    
import streamlit as st
from langchain.vectorstores import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings

from session_keys import ensure_keys_in_session

# Elasticsearch vectorstore Setup
def connect_vector_store():
    """Connect to Elasticsearch vector store."""
    # if not st.session_state["elastic_database_id"] or "elastic_database_id" not in st.session_state:
    #     st.session_state["elastic_database_id"] = "ab9fc665e06642b4b2c99c5f9898e875:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDg3MzIwMzg0YWMzNzRjNTJiYmQ3YWFkYjI4NWUxNjExJDIxMDFiZTgzNjg5ODQ0MmFhMzg4ZTMzYzU5MTdmOTlh"
        
    # if not st.session_state["elastic_api_key"] or "elastic_api_key" not in st.session_state:
    #     st.session_state["elastic_api_key"] = "WUoyVkpKTUJ0ZTlkVlhESWtSVDQ6eGUwY1dzcmlSbGE4bW5iY2gxQl9CZw=="
        
    # if not st.session_state["chatbot_api_key"] or "chatbot_api_key" not in st.session_state:
    #     st.session_state["chatbot_api_key"] = "sk-JDd8XASldxnf4JlfzqcFX6IZkRp88UQSOuS6MqsBgLT3BlbkFJoaFWr04LuZoWZQlTBdTzxzbQ7tgFTD2iXbICVfLxcA"

    # os.environ["OPENAI_API_KEY"] = st.session_state["chatbot_api_key"]
    ensure_keys_in_session()
    
    try:
        embeddings = OpenAIEmbeddings()
        vector_store = ElasticsearchStore(
            es_cloud_id=st.session_state["elastic_database_id"],
            es_api_key=st.session_state["elastic_api_key"],
            index_name="openai_mit_llama_index",
            embedding=embeddings
        )
        return vector_store
    except Exception as e:
        st.error(f"Error connecting to Elasticsearch: {e}")
        return None

def fetch_all_fields(vector_store, count=2):
    """Fetch all fields for `count` documents from the Elasticsearch index."""
    try:
        # Execute a match_all query to get all fields
        response = vector_store.client.search(
            index=vector_store.index_name,
            body={
                "query": {"match_all": {}},  # Fetch all documents
                "size": count,  # Limit to `count` documents
            },
        )
        # Parse and return the full documents
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error fetching documents: {e}")
        return []

# Streamlit UI
def display_two_random_documents():
    st.title("View 2 Random Documents")
    
    # Connect to Vectorstore
    vector_store = connect_vector_store()
    if not vector_store:
        return
    
    # Fetch all fields for 2 documents
    if st.button("Load 2 Documents"):
        with st.spinner("Fetching documents..."):
            docs = fetch_all_fields(vector_store, count=2)
            if docs:
                st.write("### Retrieved Documents")
                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"**Document {i}:**")
                    st.json(doc)  # Display the entire document in JSON format
                    st.markdown("---")
            else:
                st.warning("No documents found in the index.")

def analysis():
    display_two_random_documents()
    