import os
import streamlit as st
from langchain.vectorstores import ElasticsearchStore
from langchain.embeddings.openai import OpenAIEmbeddings
from session_keys.session_keys import ensure_keys_in_session

# Elasticsearch setup
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

# Analysis Functions
def fetch_random_articles_by_source(vector_store, source, count=10):
    """Fetch random articles from a specific source."""
    query = {
        "query": {
            "function_score": {
                "query": {
                    "term": {
                        "metadata.source.keyword": source
                    }
                },
                "random_score": {}
            }
        },
        "size": count
    }
    try:
        response = vector_store.client.search(index=vector_store.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error fetching random articles: {e}")
        return []

def get_articles_by_author(vector_store, author, count=10):
    """Retrieve articles by a specific author."""
    query = {
        "query": {
            "term": {
                "metadata.author.keyword": author
            }
        },
        "size": count
    }
    try:
        response = vector_store.client.search(index=vector_store.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error retrieving articles by author: {e}")
        return []

def get_articles_after_date(vector_store, date, count=10):
    """Retrieve articles published after a specific date."""
    query = {
        "query": {
            "range": {
                "metadata.date": {
                    "gte": date
                }
            }
        },
        "size": count
    }
    try:
        response = vector_store.client.search(index=vector_store.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error retrieving articles after date: {e}")
        return []

def search_articles_by_keyword(vector_store, keyword, count=10):
    """Search articles containing a specific keyword in the text."""
    query = {
        "query": {
            "match": {
                "text": keyword
            }
        },
        "size": count
    }
    try:
        response = vector_store.client.search(index=vector_store.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error searching articles by keyword: {e}")
        return []

def search_articles_by_heading(vector_store, heading, count=10):
    """Search articles with a specific term in the heading."""
    query = {
        "query": {
            "match": {
                "metadata.heading": heading
            }
        },
        "size": count
    }
    try:
        response = vector_store.client.search(index=vector_store.index_name, body=query)
        return [hit["_source"] for hit in response["hits"]["hits"]]
    except Exception as e:
        st.error(f"Error searching articles by heading: {e}")
        return []

# Display Results
def display_results(title, docs):
    """Display results sequentially with a header."""
    if docs:
        st.write(f"### {title}")
        for i, doc in enumerate(docs, start=1):
            st.markdown(f"**Document {i}:**")
            st.json(doc)
            st.markdown("---")
    else:
        st.warning("No documents found.")

# Main Analysis Function
def analysis():
    vector_store = connect_vector_store()
    if not vector_store:
        return
    
    st.title("Elasticsearch Dataset Analysis")
    
    # Fetch random articles by source
    st.header("Fetch Random Articles by Source")
    source = st.text_input("Enter Source (e.g., 'MIT News Office')", value="MIT News Office")
    count = st.slider("Number of articles", 1, 20, 10, key="random_articles_count")
    if st.button("Fetch Random Articles"):
        with st.spinner("Fetching random articles..."):
            docs = fetch_random_articles_by_source(vector_store, source, count)
            display_results(f"Random Articles from {source}", docs)

    # Get articles by author
    st.header("Get Articles by Author")
    author = st.text_input("Enter Author Name (e.g., 'Adam Zewe')", value="Adam Zewe")
    if st.button("Get Articles by Author"):
        with st.spinner(f"Fetching articles by author {author}..."):
            docs = get_articles_by_author(vector_store, author, count)
            display_results(f"Articles by {author}", docs)

    # Get articles after date
    st.header("Get Articles After Date")
    date = st.date_input("Select Date", key="date_filter")
    if st.button("Get Articles After Date"):
        with st.spinner(f"Fetching articles after {date}..."):
            docs = get_articles_after_date(vector_store, str(date), count)
            display_results(f"Articles Published After {date}", docs)

    # Search articles by keyword
    st.header("Search Articles by Keyword")
    keyword = st.text_input("Enter Keyword (e.g., 'AI')", value="AI")
    if st.button("Search Articles by Keyword"):
        with st.spinner(f"Searching articles containing '{keyword}'..."):
            docs = search_articles_by_keyword(vector_store, keyword, count)
            display_results(f"Articles Containing '{keyword}'", docs)

    # Search articles by heading
    st.header("Search Articles by Heading")
    heading = st.text_input("Enter Heading Keyword (e.g., 'molecules')", value="molecules")
    if st.button("Search Articles by Heading"):
        with st.spinner(f"Searching articles with heading containing '{heading}'..."):
            docs = search_articles_by_heading(vector_store, heading, count)
            display_results(f"Articles with Heading Containing '{heading}'", docs)

if __name__ == "__main__":
    analysis()