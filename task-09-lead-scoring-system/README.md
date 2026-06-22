# Task 09 - CoreTech AI Lead Scoring and Service Recommendation System

## Overview

This project analyzes CoreTech client leads and assigns a score from 0 to 100 based on business-related factors. It also provides a priority label, service recommendation, and a short explanation for each lead.

## Dataset

The dataset file is `coretech_leads.csv`.

It contains 50 sample leads with these fields:

- Lead Name
- Budget
- Timeline
- Lead Source
- Company Size
- Urgency
- Requested Service

## Scoring Factors

The lead score is calculated using:

- Budget
- Timeline
- Lead Source
- Company Size
- Urgency

## Priority Labels

- High: Score 75 or above
- Medium: Score from 45 to 74
- Low: Score below 45

## Features

- Calculates lead score from 0 to 100
- Assigns High, Medium, or Low priority
- Recommends a suitable service
- Provides a short explanation for every lead
- Processes 50 sample CoreTech leads

## How to Run

Install pandas:

```bash
pip install pandas
```

Run the program:

```bash
python lead_scoring.py
```

## Screenshots

### Lead Scoring Output

![lead-scoring-output](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\lead-scoring-output.png)

### High Priority Lead
![high-priority-lead](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\high-priority-lead.png)