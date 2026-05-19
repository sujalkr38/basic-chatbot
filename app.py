import streamlit as st


def get_bot_reply(user_message):
    """Return the bot reply using simple if-elif-else logic."""
    text = user_message.lower().strip()

    if text == "hello":
        return "Hi!"

    elif text == "how are you":
        return "I am fine"

    elif text == "bye":
        return "__bye__"

    else:
        return "I don't understand"


# Page setup
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="💬",
    layout="wide",
)

# Dark modern styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(160deg, #0f1117 0%, #161b27 50%, #12151f 100%);
        }
        [data-testid="stSidebar"] {
            background: #12151f;
            border-right: 1px solid #2a3142;
        }
        [data-testid="stSidebar"] h1 {
            color: #e8eaed;
            font-size: 1.6rem;
        }
        [data-testid="stSidebar"] p {
            color: #9aa0b4;
        }
        .chat-header {
            color: #e8eaed;
            font-size: 1.75rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }
        .chat-subtitle {
            color: #9aa0b4;
            margin-bottom: 1.5rem;
        }
        div[data-testid="stChatMessage"] {
            background: transparent;
            padding: 0.35rem 0;
        }
        div[data-testid="stChatMessageContent"] {
            background: #1e2433;
            border: 1px solid #2f3648;
            border-radius: 14px;
            padding: 0.75rem 1rem;
            color: #e8eaed;
        }
        div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) div[data-testid="stChatMessageContent"] {
            background: #2d3a8c;
            border-color: #3d4db8;
        }
        .stTextInput > div > div > input {
            background: #1e2433;
            color: #e8eaed;
            border: 1px solid #2f3648;
            border-radius: 10px;
        }
        .stButton > button {
            background: #6c63ff;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.55rem 1.4rem;
            font-weight: 600;
        }
        .stButton > button:hover {
            background: #5a52e0;
            color: white;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.title("💬 Chatbot")
    st.markdown("A simple chatbot built with **Streamlit**.")
    st.markdown("---")
    st.markdown("**Try saying:**")
    st.markdown("- hello")
    st.markdown("- how are you")
    st.markdown("- bye")

# Chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False

# Main area
st.markdown('<p class="chat-header">Chat with Bot</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="chat-subtitle">Type a message and click Send to start chatting.</p>',
    unsafe_allow_html=True,
)

# Show previous messages in chat bubbles
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input area
if st.session_state.chat_ended:
    st.info("Chat ended. Refresh the page to start again.")
else:
    col1, col2 = st.columns([5, 1])

    with col1:
        user_input = st.text_input(
            "Your message",
            placeholder="Type your message here...",
            label_visibility="collapsed",
        )

    with col2:
        send_clicked = st.button("Send", use_container_width=True)

    if send_clicked and user_input.strip():
        # Add user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input.strip()}
        )

        # Get bot reply
        reply = get_bot_reply(user_input)

        if reply == "__bye__":
            st.session_state.messages.append(
                {"role": "assistant", "content": "Goodbye! See you next time."}
            )
            st.session_state.chat_ended = True
        else:
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

        st.rerun()
