import streamlit as st
import streamlit.components.v1 as components


def about():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .title-box {
            background-color: #00274D;
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .highlight {
            background-color: #f9f9f9;
            padding: 10px;
            border-left: 5px solid #00274D;
            margin: 10px 0;
            border-radius: 5px;
        }
      
        """,
        unsafe_allow_html=True
    )

    # Overview Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Overview")
    st.markdown(
        """
        The MIT News Chatbot is a conversational AI assistant designed to help you explore and query articles from 
        [MIT News](https://news.mit.edu/). Whether you’re interested in cutting-edge research, campus updates, or 
        thought leadership, the chatbot provides instant, conversational answers while retaining the context of your 
        previous questions.
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Features")
    st.markdown(
        """
        - **Conversational Q&A**: Ask questions and get contextual answers.
        - **Context Retention**: Retain the flow of conversation across multiple queries.
        - **Data Analysis**: Analyze and explore articles by authors, categories, dates, and keywords.
        """
    )

    # Visual Divider
    st.markdown("---")

    # Visual Element - MIT Logo
    st.image(
        "https://brand.mit.edu/sites/default/files/styles/image_text_2x/public/2023-08/MIT-logo-red-textandimage.png?itok=RNoAwZvy",
        caption="Powered by MIT News",
        use_container_width=True
    )
    
    # CTA to Chat Page
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Try the tool")
    st.markdown(
        """
        Curious to see it in action? Head over to the navigation bar and start exploring!
        """
    )
    # if st.button("Go to Chat Page"):
    #     st.query_params(page="Chat")

    # How It Works Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("How It Works")
    st.markdown(
        """
        <div>
        1. The chatbot retrieves articles from [MIT News](https://news.mit.edu/) and processes them for relevance.<br>
        2. Queries are analyzed and matched with the most relevant content using advanced natural language processing.<br>
        3. Previous interactions are remembered to provide coherent responses in multi-turn conversations.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Technologies Used
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Tech Stack (Python based)")
    st.markdown(
    """
    #### 📚 Project Dependencies and Documentation

    - **[OpenAI API](https://platform.openai.com/docs/)**: Provides access to language models for generating responses.
    - **[LangChain](https://docs.langchain.com/)**: A framework for building applications powered by language models.
    - **[Elasticsearch](https://www.elastic.co/guide/index.html)**: A powerful search and analytics engine used as the data storage platform and retriever for the chatbot.
    - **[Streamlit](https://docs.streamlit.io/)**: A framework for building interactive user interfaces (UI).
    """,
    unsafe_allow_html=True
)