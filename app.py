import warnings 
warnings.filterwarnings("ignore")

import streamlit as st
from analysis_page import analysis
from about_page import about
from chat_page import chat

# Configure page
st.set_page_config(
    page_title="QA Answering Bot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title and subtitle
st.title("🤖 QA Answering Bot")
st.subheader("Powered by OpenAI API")

def main():
    with st.sidebar:
        st.title("Settings")
        st.empty()
        st.title("Navigation")
        
        # Sidebar navigation
        page = st.selectbox("Select a page:",
                            options=["About", "Chat", "Analysis"],  # Dropdown options
                            index=0  # Default selection)
        )
        
    # Display the selected page name in the main area 
    if page == "About":
        about()
    elif page == "Chat":
        chat()
    else:  
        analysis()
        
if __name__=="__main__":
    # Code to execute when the script is run directly
    main()
        
# Footer
st.markdown("---")
st.markdown("**QA Answering Bot**: Built with ❤️ using [Streamlit](https://streamlit.io) and [OpenAI API](https://platform.openai.com/docs/api-reference/introduction).")