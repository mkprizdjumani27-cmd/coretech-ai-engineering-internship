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

![Model Results](<img width="832" height="545" alt="models result" src="https://github.com/user-attachments/assets/3c35d8a3-f563-4024-8dd4-ad537ad45e9a" />)


### Prediction Result

![Prediction Result](<img width="904" height="148" alt="prediction-result" src="https://github.com/user-attachments/assets/da7d9e1b-632c-44e4-9fde-dd8af2c88fc1" />)
(<img width="902" height="141" alt="prediction-result-2" src="https://github.com/user-attachments/assets/82e94c30-78ec-4ecb-93ef-8fe082a22984" />)

