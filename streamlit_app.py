import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Buddy AI Agent", page_icon="🤖")
st.title("🤖 Buddy AI Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Handle input
if prompt := st.chat_input("Ask me something..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    try:
        response = requests.post(API_URL, json={"message": prompt})
        reply = response.json().get("reply", "⚠️ No response")
    except Exception as e:
        reply = f"⚠️ Error contacting backend: {e}"

    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
