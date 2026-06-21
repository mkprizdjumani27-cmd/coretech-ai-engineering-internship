import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load the client inquiry dataset
data = pd.read_csv("coretech_client_inquiries.csv")

# Separate messages and categories
X = data["Message"]
y = data["Category"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create a text classification pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Predict categories for test messages
predictions = model.predict(X_test)

# Show accuracy
accuracy = accuracy_score(y_test, predictions)
print("\nCoreTech Client Inquiry Text Classification System")
print("-" * 55)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Show detailed classification report
print("\nClassification Report:\n")
print(classification_report(y_test, predictions, zero_division=0))

# Test the model with a new client message
new_message = input("\nEnter a client inquiry: ")

predicted_category = model.predict([new_message])[0]

print("\nPredicted Category:", predicted_category)