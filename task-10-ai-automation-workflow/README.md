# Task 10 - AI Automation Workflow for Client Inquiries

## Overview

This project automates the processing of client inquiry messages for CoreTech Innovation.

The system reads inquiry messages, extracts important client information, identifies the requested service, assigns priority, generates a professional reply, and saves processed results in a CSV file.

## Input Dataset

The input file is `client_inquiries.csv`.

It contains client inquiry messages with an inquiry ID.

## Extracted Information

The system extracts:

- Client name
- Email address
- Required service
- Budget
- Timeline
- Urgency
- Priority label
- Professional reply

## Supported Services

- E-commerce Website
- Mobile App Development
- Web Development
- SEO
- UI/UX Design
- Custom Software Development
- Digital Marketing
- AI Chatbot Development

## Priority Rules

Priority is assigned using budget, timeline, and urgency.

- High priority: Score 75 or above
- Medium priority: Score from 45 to 74
- Low priority: Score below 45

## Features

- Reads client inquiry messages from CSV
- Extracts client details using Python regular expressions
- Identifies the required CoreTech service
- Assigns a High, Medium, or Low priority label
- Generates a professional reply template
- Saves final processed results in `processed_inquiries.csv`

## How to Run

Install pandas:

```bash
pip install pandas
```

Run the project:

```bash
python automation_workflow.py
```

## Output File

After running the program, the system creates:

```text
processed_inquiries.csv
```

## Screenshots

### Automation Output

![automation-output](<img width="901" height="714" alt="Screenshot 2026-06-23 004653" src="https://github.com/user-attachments/assets/c3c62b24-b6a8-463d-a796-d1ddfd283d14" />)


### Processed Results CSV

![processed-results-csv-output](<img width="943" height="992" alt="Screenshot 2026-06-23 004816" src="https://github.com/user-attachments/assets/b52f001d-cc5f-4b7d-aa7a-aa4b82432b27" />)
