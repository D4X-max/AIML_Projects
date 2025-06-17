import streamlit as st
import requests

st.set_page_config(page_title="AI Career Counsellor", page_icon="💬", layout="centered")

# CSS for background and chat bubbles
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%);
    }
    .chat-bubble {
        padding: 12px 18px;
        border-radius: 18px;
        margin-bottom: 8px;
        max-width: 75%;
        font-size: 1.05rem;
        word-break: break-word;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .user-bubble {
        background: #DCF8C6;
        margin-left: 25%;
        text-align: right;
        border-bottom-right-radius: 4px;
    }
    .bot-bubble {
        background: #F1F0F0;
        margin-right: 25%;
        text-align: left;
        border-bottom-left-radius: 4px;
    }
    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: inline-block;
        vertical-align: middle;
        margin-right: 8px;
        margin-left: 8px;
    }
    .chat-row {
        display: flex;
        align-items: flex-end;
        margin-bottom: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def send_message():
    user_message = st.session_state.user_input.strip()
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
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
    st.session_state.user_input = ""

st.markdown("<h2 style='text-align: center; color: #0B3D91;'>💬 AI Career Counsellor</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Get personalized career advice in a chat format!</p>", unsafe_allow_html=True)

# Display chat messages as styled bubbles with avatars
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div class="chat-row" style="justify-content: flex-end;">
                <div class="chat-bubble user-bubble">
                    <span style="font-size:1.2em;">🧑‍💻</span> {msg['content']}
                </div>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-row" style="justify-content: flex-start;">
                <div class="chat-bubble bot-bubble">
                    <span style="font-size:1.2em;">🤖</span> {msg['content']}
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# Input box at the bottom
st.text_input(
    "Type your message...",
    key="user_input",
    on_change=send_message,
    label_visibility="collapsed",
    placeholder="Type your message and press Enter..."
)


