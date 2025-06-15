import streamlit as st
import requests

st.set_page_config(page_title="AI Career Counsellor", page_icon="💬")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def send_message():
    user_message = st.session_state.user_input.strip()
    if user_message:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_message})
        # Send to Rasa backend
        try:
            response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook",
                json={"sender": "user", "message": user_message},
                timeout=10
            )
            if response.status_code == 200:
                bot_msgs = response.json()
                for bot_msg in bot_msgs:
                    if "text" in bot_msg:
                        st.session_state.messages.append({"role": "bot", "content": bot_msg["text"]})
            else:
                st.session_state.messages.append({"role": "bot", "content": "Sorry, I couldn't reach the backend."})
        except Exception as e:
            st.session_state.messages.append({"role": "bot", "content": f"Error: {e}"})
    # Clear input box after sending
    st.session_state.user_input = ""

st.markdown("<h2 style='text-align: center;'>💬 AI Career Counsellor</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask me about your career interests!</p>", unsafe_allow_html=True)

# Display chat history as bubbles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div style='background: #DCF8C6; color: black; text-align: right; padding: 10px 15px; border-radius: 15px; margin-bottom: 5px; margin-left: 80px;'><b>You:</b> {msg['content']}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='background: #F1F0F0; color: black; text-align: left; padding: 10px 15px; border-radius: 15px; margin-bottom: 5px; margin-right: 80px;'><b>Bot:</b> {msg['content']}</div>",
            unsafe_allow_html=True,
        )

# Input box at the bottom
st.text_input(
    "Type your message...",
    key="user_input",
    on_change=send_message,
    label_visibility="collapsed",
    placeholder="Type your message and press Enter..."
)


