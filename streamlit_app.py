import streamlit as st
from agent import Assistant  # your AI assistant

# Page configuration
st.set_page_config(page_title="Friday Jarvis", page_icon="🤖", layout="centered")

st.title("🤖 Friday Jarvis Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box at the bottom
if prompt := st.chat_input("Ask me something..."):
    # Store user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Call your AI Assistant
    bot = Assistant()
    response = bot.run(prompt)  # Adjust according to your agent.py logic

    # Store bot reply
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
