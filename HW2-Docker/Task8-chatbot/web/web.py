import os
import time
import requests
import streamlit as st

# Examples are from https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps

BASE_URL = os.getenv("LLM_URL", "http://localhost:12434/v1/")
MODEL = os.getenv("LLM_MODEL", "ai/smollm2:360M-Q4_K_M")
URL = BASE_URL.rstrip("/") + "/chat/completions"
HEADERS = {"Content-Type": "application/json"}

st.title("My LLM chatbot")
st.caption(f"Model: {MODEL}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, human! Is there anything I can help you with?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        placeholder = st.empty()
        data = {
            "model": MODEL,
            "messages": [{"role": "system", "content": "You are a helpful assistant."}]
            + st.session_state.messages,
        }
        try:
            resp = requests.post(URL, headers=HEADERS, json=data, timeout=120)
            resp.raise_for_status()
            answer = resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            answer = f"LLM request failed: {e}"

        shown = ""
        for word in answer.split():
            shown += word + " "
            time.sleep(0.03)
            placeholder.markdown(shown)
        placeholder.markdown(answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})
