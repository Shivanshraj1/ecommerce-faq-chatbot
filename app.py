import streamlit as st

from chatbot import FAQChatbot


st.set_page_config(
    page_title="E-commerce FAQ Chatbot",
    page_icon="💬",
    layout="centered",
)


@st.cache_resource
def load_chatbot():
    return FAQChatbot()


chatbot = load_chatbot()

st.title("E-commerce FAQ Chatbot")
st.write(
    "Ask a customer-support question about orders, delivery, payments, returns, "
    "refunds, accounts, or products."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me an e-commerce support question.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Type your question here...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    response = chatbot.get_response(user_question)
    bot_message = response["answer"]

    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.write(bot_message)

        if response["matched_question"]:
            with st.expander("Match details"):
                st.write(f"Matched FAQ: {response['matched_question']}")
                st.write(f"Category: {response['category']}")
                st.write(f"Similarity score: {response['score']}")
