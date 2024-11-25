import os
from typing import List, Any
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseRetriever, Document
from langchain.chains import create_history_aware_retriever
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from pydantic import Field
from elastic_connect import retrieve_vector_store
import streamlit as st

from session_keys import ensure_keys_in_session

# Lazy initialization of LLM
def get_llm():
    # if "chatbot_api_key" not in st.session_state or not st.session_state["chatbot_api_key"]:
    #     # If the API key is missing, return None (or handle it silently)
    #     st.session_state["chatbot_api_key"] = "sk-JDd8XASldxnf4JlfzqcFX6IZkRp88UQSOuS6MqsBgLT3BlbkFJoaFWr04LuZoWZQlTBdTzxzbQ7tgFTD2iXbICVfLxcA"
    # # Set the OpenAI API key as an environment variable
    # os.environ["OPENAI_API_KEY"] = st.session_state["chatbot_api_key"]
    ensure_keys_in_session()
    # Initialize and return the LLM instance
    return ChatOpenAI(model="gpt-4o-mini")

# Use `get_llm` to retrieve the LLM instance when needed
LLM = get_llm()

class HeadingBasedRetriever(BaseRetriever):
    vector_store: Any
    top_k: int = Field(default=1)

    def _get_relevant_documents(self, query: str) -> List[Document]:
        results = self.vector_store.similarity_search(
            query=query,
            k=self.top_k,
            filter=None  # Optional: Add filters if needed
        )
        if results:
            top_result = results[0]
            return [Document(page_content=top_result.page_content, metadata=top_result.metadata)]
        return []

# Initialize the vector store lazily
def rag():
    vector_store = retrieve_vector_store()
    if vector_store and LLM:  # Proceed only if prerequisites are available
        retriever = HeadingBasedRetriever(vector_store=vector_store)

        context_q_system_prompt = (
            """
                Given a chat history and the latest user question which might reference context in the chat history as well as in the external retrieved context given here,
                formulate a standalone question which can be understood without the chat history. Do NOT answer the question,
                just reformulate it if needed and otherwise return it as is. Be verbose and yet educational in your response.
            """
        )

        context_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", context_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        history_aware_retriever = create_history_aware_retriever(
            LLM, retriever, context_q_prompt
        )

        system_prompt = (
            """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Be as precise, accurate and educational in your response as possible.
                context: {context}
                Answer:
            """
        )

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(LLM, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        
        return rag_chain

def get_response():
    """Get a response from the ChatGPT API."""
    pass