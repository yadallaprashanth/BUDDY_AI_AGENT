import streamlit as st

# Try importing the real Assistant
try:
    from agent import Assistant
    USE_REAL_ASSISTANT = True
except RuntimeError:
    # Fallback stub if plugin registration fails
    class Assistant:
        def run(self, message: str):
            return f"(Stub response) You said: {message}"
    USE_REAL_ASSISTANT = False

st.set_page_config(page_title="Buddy AI Agent", page_icon="🤖")

st.title("🤖 Buddy AI Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input
if prompt := st.chat_input("Ask me something..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Assistant response
    bot = Assistant()
    response = bot.run(prompt) if USE_REAL_ASSISTANT else bot.run(prompt)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
