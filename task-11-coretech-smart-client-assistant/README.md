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

## AI Workflow

The application follows the workflow below:

1. The user enters a client inquiry.
2. The system preprocesses the input text.
3. TF-IDF Vectorizer converts the text into numerical vectors.
4. Cosine Similarity searches the knowledge base and finds the most relevant information.
5. Rule-based logic extracts:
   - Client Name
   - Email Address
   - Required Service
   - Budget
   - Timeline
   - Urgency
6. A lead score (0–100) is calculated.
7. The system assigns High, Medium, or Low priority.
8. A professional business reply is generated.
9. The processed inquiry is stored in processed_inquiries.csv.

## Dataset

The project uses a custom dataset named:

coretech_knowledge_base.csv

The dataset contains:

- Company Profile
- Services
- FAQs
- Pricing Information
- Project Workflow
- Contact Details

This dataset is used for semantic search using TF-IDF and Cosine Similarity.

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
## Future Improvements

- Integrate Large Language Models (LLMs)
- Add voice-based client interaction
- Store data in a SQL database
- Deploy the application on Streamlit Cloud
- Add user authentication
- Build an admin dashboard

## Learning Outcomes

Through this project, I learned:

- Building Streamlit web applications
- Semantic search using TF-IDF
- Cosine Similarity
- Rule-based AI systems
- Lead scoring techniques
- Data preprocessing
- CSV data storage
- AI workflow design

## Author

MUHAMMAD JUMANI

Final AI Engineering Internship Project

CoreTech Innovation

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

![home-screen]((c:\Users\Dell Latitude E5490\OneDrive - MUET\Desktop\task-09-lead-scoring-system\home-screen.png))

### Sample Output (1)

![sample-output(1)]((sc:\Users\Dell Latitude E5490\OneDrive - MUET\Desktop\task-09-lead-scoring-system\sample-output (1).png))

### Sample Output (2)

![sample-output(2)]((c:\Users\Dell Latitude E5490\OneDrive - MUET\Desktop\task-09-lead-scoring-system\sample-output (2).png))

### Processed Data

![processed-data]((c:\Users\Dell Latitude E5490\OneDrive - MUET\Desktop\task-09-lead-scoring-system\processed-data.png))

