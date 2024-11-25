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
        .feedback-btn {
            background-color: #00274D;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .feedback-btn:hover {
            background-color: #00509e;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title Section
    st.markdown(
        """
        <div class="title-box">
            <h1>Welcome to the MIT News Chatbot</h1>
            <p>Your intelligent assistant for exploring MIT News articles</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Overview Section
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

    # Features Section
    st.subheader("Key Features")
    features = [
        "**Comprehensive Knowledge**: Access the latest articles and archives from MIT News.",
        "**Conversational AI**: Retains the context of your queries for a seamless experience.",
        "**Effortless Search**: Type your question, and the bot retrieves and synthesizes relevant information."
    ]
    for feature in features:
        st.markdown(f"- {feature}")

    # Visual Divider
    st.markdown("---")

    # Visual Element - MIT Logo
    # st.image(
    #     "https://news.mit.edu/sites/all/themes/mit2016/images/logo-black.svg",
    #     caption="Powered by MIT News",
    #     use_container_width=True
    # )

    # CTA to Chat Page
    st.subheader("Try the Chatbot")
    st.markdown(
        """
        Curious to see it in action? Head over to the **Chat Page** from the navigation bar and start exploring!
        """
    )
    # if st.button("Go to Chat Page"):
    #     st.query_params(page="Chat")

    # How It Works Section
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

    # Feedback Section
    st.subheader("Have Feedback?")
    st.markdown("We'd love to hear your thoughts! Share your feedback below:")
    components.html(
        """
        <form action="https://formspree.io/f/xknypbwp" method="POST">
            <textarea name="feedback" rows="4" cols="40" placeholder="Type your feedback here..." style="width:100%; margin-bottom: 10px;"></textarea><br>
            <button type="submit" class="feedback-btn">Submit Feedback</button>
        </form>
        """,
        height=200
    )