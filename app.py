import streamlit as st
import requests

st.title("📅 Appointment Booking Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("Ask something like:")
st.code("What time am I free tomorrow?\nBook a meeting")

# Chat loop
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    msg_text = user_input.lower()  # 👈 renamed to avoid conflict

    if any(word in msg_text for word in ["free", "available", "schedule", "when", "time"]):
        response = requests.get("http://127.0.0.1:8000/free-slots")
        bot_reply = response.json()["available_slots"]
    elif any(word in msg_text for word in ["book", "meeting", "appointment", "reserve", "slot"]):
        response = requests.post("http://127.0.0.1:8000/book")
        bot_reply = response.json()["status"]
    else:
        bot_reply = "Sorry, I can only help with checking free time or booking right now."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat history
for chat_msg in st.session_state.messages:  # 👈 renamed from msg to chat_msg
    if chat_msg["role"] == "user":
        st.markdown(f"👤 **You:** {chat_msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {chat_msg['content']}")

