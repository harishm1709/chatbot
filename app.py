import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyBIZASc3i7WggMaityBq93UUt_cdTknFPQ")

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini Chatbot")
st.title("🤖 natham AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Gemini response
    response = model.generate_content(user_input)
    bot_reply = response.text

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
