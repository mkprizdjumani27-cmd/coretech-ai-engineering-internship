import pandas as pd

# Load lead dataset
leads = pd.read_csv("coretech_leads.csv")

def calculate_lead_score(lead):
    score = 0

    # Budget scoring
    budget_scores = {"High": 30, "Medium": 20, "Low": 10}
    score += budget_scores.get(lead["Budget"], 0)

    # Timeline scoring
    timeline_scores = {"Immediate": 25, "1 Month": 20, "2 Months": 10, "3 Months": 5}
    score += timeline_scores.get(lead["Timeline"], 0)

    # Lead source scoring
    source_scores = {
        "Referral": 20,
        "Website": 15,
        "LinkedIn": 15,
        "Google": 10,
        "Facebook": 5,
        "Instagram": 5
    }
    score += source_scores.get(lead["Lead_Source"], 0)

    # Company size scoring
    company_scores = {"Large": 15, "Medium": 10, "Small": 5}
    score += company_scores.get(lead["Company_Size"], 0)

    # Urgency scoring
    urgency_scores = {"High": 10, "Medium": 5, "Low": 0}
    score += urgency_scores.get(lead["Urgency"], 0)

    return min(score, 100)


def get_priority(score):
    if score >= 75:
        return "High"
    elif score >= 45:
        return "Medium"
    else:
        return "Low"


def recommend_service(requested_service):
    return requested_service


def create_explanation(lead, score, priority):
    return (
        f"This lead has a {lead['Budget'].lower()} budget, "
        f"{lead['Timeline'].lower()} timeline, "
        f"{lead['Urgency'].lower()} urgency, and is from a "
        f"{lead['Company_Size'].lower()} company. "
        f"Therefore, it received a {priority.lower()} priority score of {score}/100."
    )


print("CoreTech AI Lead Scoring and Service Recommendation System")
print("-" * 65)

for _, lead in leads.iterrows():
    score = calculate_lead_score(lead)
    priority = get_priority(score)
    recommendation = recommend_service(lead["Requested_Service"])
    explanation = create_explanation(lead, score, priority)

    print(f"\nLead Name: {lead['Lead_Name']}")
    print(f"Lead Score: {score}/100")
    print(f"Priority: {priority}")
    print(f"Service Recommendation: {recommendation}")
    print(f"Explanation: {explanation}")
    print("-" * 65)