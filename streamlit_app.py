# app.py
import streamlit as st
import requests
import sseclient

st.title("Streamlit MCP Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Say something..."):
    # Display user message in chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulate sending a request to MCP server
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            # Connect to the SSE endpoint of the MCP server
            with requests.get("http://localhost:8080/sse", stream=True) as response:
                client = sseclient.SSEClient(response)
                for event in client.events():
                    if event.data:
                        full_response += event.data + " "
                        message_placeholder.markdown(full_response + "▌")
        except requests.exceptions.ConnectionError:
            full_response = "Error: Could not connect to MCP server. Is it running?"
        
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})