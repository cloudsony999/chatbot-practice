import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
print('hi')

try:
     # loading the environment variables from the .env file that contains the Google API key.
    load_dotenv(find_dotenv(), override=True)

    # configuring the generative AI model to use the GOOGLE_API_KEY for authentication.
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

    print('hi')
      
    model = genai.GenerativeModel('gemini-pro')

    if "chat" not in st.session_state:
      st.session_state.chat = model.start_chat(history=[])
    st.title('Gemini Pro Test')

    def role_to_streamlit(role: str) -> str:
      if role == 'model':
        return 'assistant'
      else:
        return role

    for message in st.session_state.chat.history:
      with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

    if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
      st.chat_message("user").markdown(prompt)
      response = st.session_state.chat.send_message(prompt)
      with st.chat_message("assistant"):
        st.markdown(response.text)
except Exception as e:
    st.error(f'An error occurred: {e}')