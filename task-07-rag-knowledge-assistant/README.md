# Task 07 - CoreTech RAG-Style Knowledge Assistant

## Overview

This project is a RAG-style knowledge assistant for CoreTech. It searches multiple knowledge base documents and returns the most relevant information for a user question.

## How It Works

1. The program reads five CoreTech knowledge documents.
2. TF-IDF converts document text into numerical vectors.
3. Cosine Similarity compares the user question with all documents.
4. The most relevant document content is returned.
5. The source document name is displayed with the answer.

## Knowledge Base Documents

- company_profile.txt
- services.txt
- project_process.txt
- pricing_sample.txt
- faqs.txt

## Features

- Accepts a user question
- Searches relevant CoreTech information
- Uses TF-IDF vectorization
- Uses Cosine Similarity
- Returns the most relevant document content
- Shows the source document used

## Technologies Used

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## How to Run

Install the required library:

```bash
pip install scikit-learn

## Screenshots

### FAQ Result
![FAQ](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\faqs.txt.png)

### Pricing Sample Result
![Pricing Sample](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\pricing_sample.txt.png)