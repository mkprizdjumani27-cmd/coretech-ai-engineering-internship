# CoreTech Smart Client Assistant

## Final AI Engineering Project

CoreTech Smart Client Assistant is an AI-powered business support system designed for CoreTech Innovation.

It combines customer support, semantic search, service recommendation, client detail extraction, lead scoring, priority assignment, professional reply generation, and CSV-based inquiry record storage in one Streamlit web application.

## Problem Statement

Businesses receive many client messages every day. Manually reading every message, identifying the required service, checking urgency, deciding priority, and preparing replies can take time.

This project automates that workflow for CoreTech Innovation.

## Main Features

- Accepts client inquiries through a Streamlit web interface
- Searches a CoreTech knowledge base using TF-IDF and cosine similarity
- Finds relevant company information for the inquiry
- Identifies the required service
- Extracts client name and email address
- Detects budget, timeline, and urgency
- Calculates a lead score from 0 to 100
- Assigns High, Medium, or Low priority
- Generates a professional reply template
- Saves every processed inquiry in `processed_inquiries.csv`

## Supported Services

- Web Development
- E-commerce Website Development
- Mobile App Development
- UI/UX Design
- SEO Services
- Digital Marketing
- Custom Software Development
- AI Chatbot Development
- Business Automation

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Regular Expressions

## Project Files

```text
task-11-coretech-smart-client-assistant
├── app.py
├── coretech_knowledge_base.csv
├── processed_inquiries.csv
├── requirements.txt
├── README.md
└── screenshots
```

## How to Run

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Example Inquiry

```text
My name is Muhammad Khan. My email is muhammad@gmail.com.
I need an e-commerce website for my clothing business.
My budget is high and I need it immediately.
```

## Example Output

```text
Recommended Service: E-commerce Website Development
Lead Score: 100/100
Priority: High
```

## Screenshots

### Application Home Screen

![195200](![alt text](<Screenshot 2026-06-24 195200.png>))

### High Priority Lead Analysis

![195000](![alt text](<Screenshot 2026-06-24 195000-2.png>))

### Saved Processed Inquiries

![195319](![alt text](<Screenshot 2026-06-24 195319.png>))
