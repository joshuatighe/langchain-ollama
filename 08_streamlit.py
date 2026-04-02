import streamlit as st
from langchain_ollama import OllamaLLM

st.title("Simple Ollama Chat")

llm = OllamaLLM(model="tinyllama:latest")

user_input = st.text_input("You:")

if st.button("Send") and user_input.strip():
    with st.spinner("Thinking..."):
        response = llm.invoke(user_input)
    st.markdown(f"**AI:** {response}")