import streamlit as st

st.set_page_config(page_title="Buddy AI Agent", page_icon="🤖", layout="centered")
st.title("🤖 Buddy AI Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Ask me something..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # 🔹 Import Assistant only when needed
    from agent import Assistant  
    bot = Assistant()
    response = bot.run(prompt)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
