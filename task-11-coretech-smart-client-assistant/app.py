import streamlit as st
import pandas as pd
import re
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page settings
st.set_page_config(
    page_title="CoreTech Smart Client Assistant",
    page_icon="🤖",
    layout="wide"
)

# Load knowledge base
@st.cache_data
def load_knowledge_base():
    return pd.read_csv("coretech_knowledge_base.csv")

knowledge_base = load_knowledge_base()

# Create semantic search model
vectorizer = TfidfVectorizer(stop_words="english")
knowledge_vectors = vectorizer.fit_transform(knowledge_base["Content"])


def find_relevant_answer(user_message):
    user_vector = vectorizer.transform([user_message])
    similarity_scores = cosine_similarity(user_vector, knowledge_vectors).flatten()

    best_index = similarity_scores.argmax()
    best_score = similarity_scores[best_index]

    answer = knowledge_base.iloc[best_index]["Content"]
    category = knowledge_base.iloc[best_index]["Category"]

    return answer, category, best_score


def extract_name(message):
    patterns = [
        r"my name is ([A-Za-z ]+?)(?:\.|,| and| my email)",
        r"i am ([A-Za-z ]+?)(?:\.|,| and|\. my)",
        r"this is ([A-Za-z ]+?)(?:\.|,|\. my)"
    ]

    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.group(1).strip().title()

    return "Valued Client"


def extract_email(message):
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", message)

    if match:
        return match.group()

    return "Not Provided"


def identify_service(message):
    message = message.lower()

    service_keywords = {
        "E-commerce Website Development": [
            "e-commerce", "ecommerce", "online store", "shopping cart",
            "online payments", "product catalog"
        ],
        "Mobile App Development": [
            "mobile app", "android app", "iphone app", "ios app",
            "food delivery app", "application"
        ],
        "Web Development": [
            "website", "web development", "business website",
            "portfolio website", "website redesign", "landing page"
        ],
        "SEO Services": [
            "seo", "google ranking", "search engine", "organic traffic",
            "keywords", "website ranking"
        ],
        "UI/UX Design": [
            "ui ux", "ui/ux", "user interface", "user experience",
            "wireframe", "prototype", "dashboard design"
        ],
        "Custom Software Development": [
            "custom software", "inventory system", "billing system",
            "management system", "employee system", "automation"
        ],
        "Digital Marketing": [
            "digital marketing", "social media marketing", "facebook ads",
            "instagram marketing", "online ads", "brand awareness"
        ],
        "AI Chatbot Development": [
            "ai chatbot", "chatbot", "customer support bot",
            "faq bot", "virtual assistant"
        ]
    }

    for service, keywords in service_keywords.items():
        for keyword in keywords:
            if keyword in message:
                return service

    return "General Consultation"


def extract_budget(message):
    message = message.lower()

    if "high budget" in message or "budget is high" in message:
        return "High"
    elif "medium budget" in message or "budget is medium" in message:
        return "Medium"
    elif "low budget" in message or "budget is low" in message:
        return "Low"

    return "Not Mentioned"


def extract_timeline(message):
    message = message.lower()

    if "immediately" in message or "as soon as possible" in message:
        return "Immediate"
    elif "1 month" in message or "one month" in message:
        return "1 Month"
    elif "2 months" in message or "two months" in message:
        return "2 Months"
    elif "3 months" in message or "three months" in message:
        return "3 Months"

    return "Not Mentioned"


def extract_urgency(message):
    message = message.lower()

    if "urgent" in message or "immediately" in message or "as soon as possible" in message:
        return "High"
    elif "1 month" in message or "one month" in message:
        return "Medium"
    elif "2 months" in message or "two months" in message:
        return "Medium"
    elif "3 months" in message or "three months" in message:
        return "Low"

    return "Medium"


def calculate_lead_score(budget, timeline, urgency):
    budget_scores = {
        "High": 40,
        "Medium": 25,
        "Low": 10,
        "Not Mentioned": 15
    }

    timeline_scores = {
        "Immediate": 30,
        "1 Month": 20,
        "2 Months": 10,
        "3 Months": 5,
        "Not Mentioned": 10
    }

    urgency_scores = {
        "High": 30,
        "Medium": 15,
        "Low": 5
    }

    score = (
        budget_scores.get(budget, 15)
        + timeline_scores.get(timeline, 10)
        + urgency_scores.get(urgency, 15)
    )

    return min(score, 100)


def get_priority(score):
    if score >= 75:
        return "High"
    elif score >= 45:
        return "Medium"
    return "Low"


def generate_reply(name, service, priority):
    return (
        f"Dear {name}, thank you for contacting CoreTech Innovation. "
        f"We have received your inquiry regarding {service}. "
        f"Your request has been marked as {priority} priority. "
        f"Our team will review your requirements and contact you soon. "
        f"Best regards, CoreTech Innovation Team."
    )


def save_inquiry(data):
    file_name = "processed_inquiries.csv"

    try:
        old_data = pd.read_csv(file_name)
        updated_data = pd.concat([old_data, pd.DataFrame([data])], ignore_index=True)
        updated_data.to_csv(file_name, index=False)
    except FileNotFoundError:
        pd.DataFrame([data]).to_csv(file_name, index=False)


# App interface
st.title("🤖 CoreTech Smart Client Assistant")
st.subheader("AI-Powered Support, Service Recommendation and Lead Prioritization")

st.write(
    "Ask a question or describe your project. The assistant will find relevant information, "
    "recommend a service, analyze lead priority, and generate a professional reply."
)

st.divider()

with st.sidebar:
    st.header("CoreTech Services")
    st.write("• Web Development")
    st.write("• E-commerce Websites")
    st.write("• Mobile App Development")
    st.write("• UI/UX Design")
    st.write("• SEO Services")
    st.write("• Digital Marketing")
    st.write("• Custom Software")
    st.write("• AI Chatbots")
    st.write("• Business Automation")

user_message = st.text_area(
    "Enter your inquiry",
    placeholder=(
        "Example: My name is Muhammad. My email is muhammad@gmail.com. "
        "I need an e-commerce website. My budget is high and I need it immediately."
    ),
    height=150
)

if st.button("Analyze Inquiry", use_container_width=True):
    if user_message.strip() == "":
        st.warning("Please enter a client inquiry first.")
    else:
        answer, category, similarity_score = find_relevant_answer(user_message)

        name = extract_name(user_message)
        email = extract_email(user_message)
        service = identify_service(user_message)
        budget = extract_budget(user_message)
        timeline = extract_timeline(user_message)
        urgency = extract_urgency(user_message)

        lead_score = calculate_lead_score(budget, timeline, urgency)
        priority = get_priority(lead_score)
        professional_reply = generate_reply(name, service, priority)

        st.success("Inquiry analyzed successfully.")

        left_column, right_column = st.columns(2)

        with left_column:
            st.subheader("Client Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Required Service:** {service}")
            st.write(f"**Budget:** {budget}")
            st.write(f"**Timeline:** {timeline}")
            st.write(f"**Urgency:** {urgency}")

        with right_column:
            st.subheader("Lead Analysis")
            st.metric("Lead Score", f"{lead_score}/100")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Recommended Service:** {service}")
            st.write(f"**Knowledge Base Category:** {category}")
            st.write(f"**Similarity Score:** {similarity_score:.2f}")

        st.subheader("Relevant CoreTech Information")
        st.info(answer)

        st.subheader("Professional Reply")
        st.write(professional_reply)

        inquiry_data = {
            "Date_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Client_Name": name,
            "Email": email,
            "Inquiry": user_message,
            "Required_Service": service,
            "Budget": budget,
            "Timeline": timeline,
            "Urgency": urgency,
            "Lead_Score": lead_score,
            "Priority": priority,
            "Knowledge_Base_Category": category,
            "Similarity_Score": round(float(similarity_score), 2),
            "Professional_Reply": professional_reply
        }

        save_inquiry(inquiry_data)

        st.caption("This inquiry has been saved successfully in processed_inquiries.csv.")