import pandas as pd
import re

# Read client inquiry messages
inquiries = pd.read_csv("client_inquiries.csv")


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
    return "Not Found"


def identify_service(message):
    message = message.lower()

    service_keywords = {
        "E-commerce Website": ["e-commerce", "online store", "online payments"],
        "Mobile App Development": ["mobile app", "android app", "iphone app", "food delivery"],
        "Web Development": ["website", "website redesign", "business website"],
        "SEO": ["seo", "ranking on google", "google ranking"],
        "UI/UX Design": ["ui ux", "ui/ux", "user interface", "user experience"],
        "Custom Software Development": ["custom software", "inventory management", "management system"],
        "Digital Marketing": ["digital marketing", "social media marketing", "social media"],
        "AI Chatbot Development": ["ai chatbot", "chatbot", "customer support"]
    }

    for service, keywords in service_keywords.items():
        for keyword in keywords:
            if keyword in message:
                return service

    return "General Consultation"


def extract_budget(message):
    message = message.lower()

    if "budget is high" in message or "high budget" in message:
        return "High"
    elif "budget is medium" in message or "medium budget" in message:
        return "Medium"
    elif "budget is low" in message or "low budget" in message:
        return "Low"

    return "Not Mentioned"


def extract_timeline(message):
    message = message.lower()

    if "immediately" in message:
        return "Immediate"
    elif "1 month" in message:
        return "1 Month"
    elif "2 months" in message:
        return "2 Months"
    elif "3 months" in message:
        return "3 Months"

    return "Not Mentioned"


def extract_urgency(message):
    message = message.lower()

    if "urgent" in message or "immediately" in message:
        return "High"
    elif "1 month" in message:
        return "Medium"
    elif "2 months" in message:
        return "Medium"
    elif "3 months" in message:
        return "Low"

    return "Medium"


def assign_priority(budget, timeline, urgency):
    score = 0

    budget_scores = {"High": 40, "Medium": 25, "Low": 10}
    timeline_scores = {"Immediate": 30, "1 Month": 20, "2 Months": 10, "3 Months": 5}
    urgency_scores = {"High": 30, "Medium": 15, "Low": 5}

    score += budget_scores.get(budget, 10)
    score += timeline_scores.get(timeline, 5)
    score += urgency_scores.get(urgency, 10)

    if score >= 75:
        return "High"
    elif score >= 45:
        return "Medium"
    else:
        return "Low"


def generate_reply(name, service, priority):
    return (
        f"Dear {name}, thank you for contacting CoreTech Innovation. "
        f"We have received your inquiry regarding {service}. "
        f"Your request has been marked as {priority} priority. "
        f"Our team will review your requirements and contact you soon. "
        f"Best regards, CoreTech Innovation Team."
    )


processed_results = []

for _, row in inquiries.iterrows():
    message = row["Message"]

    name = extract_name(message)
    email = extract_email(message)
    service = identify_service(message)
    budget = extract_budget(message)
    timeline = extract_timeline(message)
    urgency = extract_urgency(message)
    priority = assign_priority(budget, timeline, urgency)
    reply = generate_reply(name, service, priority)

    processed_results.append({
        "Inquiry_ID": row["Inquiry_ID"],
        "Client_Name": name,
        "Email": email,
        "Required_Service": service,
        "Budget": budget,
        "Timeline": timeline,
        "Urgency": urgency,
        "Priority": priority,
        "Professional_Reply": reply
    })

    print("\n" + "=" * 70)
    print(f"Inquiry ID: {row['Inquiry_ID']}")
    print(f"Client Name: {name}")
    print(f"Email: {email}")
    print(f"Required Service: {service}")
    print(f"Budget: {budget}")
    print(f"Timeline: {timeline}")
    print(f"Urgency: {urgency}")
    print(f"Priority: {priority}")
    print(f"Professional Reply: {reply}")

# Save final processed results
processed_df = pd.DataFrame(processed_results)
processed_df.to_csv("processed_inquiries.csv", index=False)

print("\n" + "=" * 70)
print("Automation completed successfully.")
print("Processed results saved in processed_inquiries.csv")