# Task 08 - CoreTech Client Inquiry Text Classification System

## Overview

This project classifies client inquiries into different CoreTech service categories using machine learning.

## Categories

- Web Development
- App Development
- UI/UX Design
- Digital Marketing
- SEO
- Software Solutions
- General Inquiry
- Complaint

## Dataset

The dataset file is `coretech_client_inquiries.csv`.

It contains 64 client messages, with 8 messages for each category.

## Machine Learning Model

This project uses:

- TF-IDF Vectorizer for converting text into numerical features
- Multinomial Naive Bayes for text classification
- Train-test split for model evaluation

## Features

- Classifies client messages into 8 categories
- Displays model accuracy
- Displays a classification report
- Predicts the category of a new client inquiry

## How to Run

Install required libraries:

```bash
pip install pandas scikit-learn
```

Run the program:

```bash
python text_classification.py
```

## Example

Input:

```text
I need an online store website for my business
```

Output:

```text
Predicted Category: Web Development
```

## Screenshots

### Model Results

![Model Results](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\models.result.png)

### Prediction Result

![Prediction Result](c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\prediction-result-2.png)
(c:\Users\Dell Latitude E5490\OneDrive - MUET\Pictures\Camera Roll\prediction-result.png)