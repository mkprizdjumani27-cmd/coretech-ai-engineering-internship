import streamlit as st
import pandas as pd

faq = pd.read_csv("coretech_faq.csv")

st.set_page_config(
    page_title="CoreTech AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 CoreTech AI Assistant")

st.markdown("### Welcome to CoreTech Innovation")
st.write("Ask about our services, solutions, projects, or contact information.")

user_question = st.text_input("Ask your question here")

if user_question:

    answer_found = False

    for index, row in faq.iterrows():

        faq_question = row["Question"].lower()

        if any(word in faq_question for word in user_question.lower().split()):

            st.success(row["Answer"])

            answer_found = True

            break

    if not answer_found:

        st.warning(
            "Sorry, I could not find information related to your question."
        )

st.markdown("---")
st.markdown("**CoreTech Innovation Virtual Assistant**")