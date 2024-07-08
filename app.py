# Q&A Chatbot 
import os
import streamlit as st
import warnings
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv() # Takes ENV variables from .env

# For Suppress specific warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.7)
    response = llm(question)
    return response

## Initialize Streamlit App ##

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")

response = get_openai_response(input)

submit = st.button("Ask the question")

## If the button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)



