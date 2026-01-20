import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)


if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
}

.chat-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 15px;
    border-radius: 15px;
    background-color: #020617;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow-y: auto;
    height: 70vh;
}

.message {
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 70%;
    word-wrap: break-word;
}

.user {
    background-color: #e5e7eb;
    color: #111827;
    margin-left: auto;   /* RIGHT */
    text-align: right;
    align-self: flex-end;
}

.bot {
    background: none;
    color: #111827;
    align-self: flex-start;
}

/* Sticky input bar at the bottom */
.stTextInput>div>div>input {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 25px;
    padding: 18px 20px;
    font-size: 18px;
    width: 100%;
}

.stTextInput {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    z-index: 100;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖AI Chatbot")
st.caption("Powered by OpenAI API")

def submit():
    user_input = st.session_state.input_text.strip()
    if user_input:
        
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        
        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_input
        )
        
        reply = response.output_text
        
        st.session_state.messages.append({"role": "bot", "content": reply})
        
        
        st.session_state.input_text = ""


chat_placeholder = st.container()

with chat_placeholder:
    for msg in st.session_state.messages:
        role_class = "user" if msg["role"] == "user" else "bot"
        st.markdown(f'<div class="message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)


st.text_input("Type your message...", key="input_text", on_change=submit)
