import streamlit as st
import requests

st.title("AI Virtual Career Counsellor")

st.write("Chat with the bot to get career recommendations based on your interests.")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send to Rasa server (update URL if needed)
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_input},
    )
    bot_reply = ""
    if response.ok and response.json():
        bot_reply = response.json()[0].get("text", "")
    else:
        bot_reply = "Sorry, I couldn't get a response from the bot."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
