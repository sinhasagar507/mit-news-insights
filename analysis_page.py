import os
import streamlit as st
from langchain.vectorstores import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings

from session_keys import ensure_keys_in_session

# Elasticsearch vectorstore Setup
def connect_vector_store():
    """Connect to Elasticsearch vector store."""
    
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
    