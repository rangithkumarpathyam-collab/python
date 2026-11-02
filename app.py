
import streamlit as st
from chatbot import get_ai_response, generate_quiz

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Buddy")
st.write("Your personal AI learning assistant!")

# Subject selection
st.sidebar.header("Study Settings")

subject = st.sidebar.selectbox(
    "Choose your subject",
    [
        "C Programming",
        "Python",
        "Java",
        "Data Structures",
        "DBMS",
        "Computer Networks",
        "Operating Systems"
    ]
)

st.sidebar.write(f"📖 Selected: {subject}")

# Navigation
page = st.sidebar.radio(
    "Choose a feature",
    ["AI Chatbot", "Quiz Generator"]
)

if page == "AI Chatbot":

    st.header("💬 Ask Your Study Buddy")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask your study question...")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            response = st.write_stream(
                get_ai_response(question, subject)
            )

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

elif page == "Quiz Generator":

    st.header("📝 AI Quiz Generator")

    st.write(f"Generate a quiz for **{subject}**.")

    if st.button("Generate 5 MCQs", type="primary"):
        with st.spinner("Generating your quiz..."):
            quiz = generate_quiz(subject)

        st.markdown(quiz)
