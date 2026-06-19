import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("coretech_knowledge_base.csv")

documents = data["Text"]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query = input("Enter your search query: ")

query_vector = vectorizer.transform([query])

similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

scores = similarity_scores[0]

top_indices = scores.argsort()[-3:][::-1]

print("\nTop 3 Matching Results:\n")

for index in top_indices:

    print("Result:", documents[index])

    print("Similarity Score:", round(scores[index], 3))

    print("-" * 50)