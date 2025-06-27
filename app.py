import streamlit as st

st.title("📅 Appointment Booking Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("Ask something like:")
st.code("What time am I free tomorrow?\nBook a meeting")

# Chat loop
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    msg_text = user_input.lower()

    if any(word in msg_text for word in ["free", "available", "schedule", "when", "time"]):
        bot_reply = "You are free tomorrow between 3 PM and 5 PM."
    elif any(word in msg_text for word in ["book", "meeting", "appointment", "reserve", "slot"]):
        bot_reply = "Your appointment has been booked successfully!"
    else:
        bot_reply = "Sorry, I can only help with checking free time or booking right now."

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display chat history
for chat_msg in st.session_state.messages:
    if chat_msg["role"] == "user":
        st.markdown(f"👤 **You:** {chat_msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {chat_msg['content']}")
