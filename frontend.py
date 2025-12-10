import streamlit as st
from main import get_groq_response

st.title("SR's Guddu Bacca  🧠")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("assistant"):
        with st.spinner("Guddu is thinking..."):
            response = get_groq_response(st.session_state.messages)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
