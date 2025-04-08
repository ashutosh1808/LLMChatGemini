from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model and get response
model=genai.GenerativeModel("gemini-1.5-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A Chat App")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
 
input=st.text_input("Input",key="input")
submit=st.button("Ask the Question")

if input and submit:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You: ",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot: ",chunk.text))



for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")