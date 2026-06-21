from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = {
    "company_profile.txt": open("company_profile.txt", "r", encoding="utf-8").read(),
    "services.txt": open("services.txt", "r", encoding="utf-8").read(),
    "project_process.txt": open("project_process.txt", "r", encoding="utf-8").read(),
    "pricing_sample.txt": open("pricing_sample.txt", "r", encoding="utf-8").read(),
    "faqs.txt": open("faqs.txt", "r", encoding="utf-8").read()
}

doc_names = list(documents.keys())
doc_contents = list(documents.values())

vectorizer = TfidfVectorizer()

doc_vectors = vectorizer.fit_transform(doc_contents)

query = input("Ask a question: ")

query_vector = vectorizer.transform([query])

similarity_scores = cosine_similarity(query_vector, doc_vectors)

best_match_index = similarity_scores.argmax()

print("\nMost Relevant Information:\n")

print(doc_contents[best_match_index])

print("\nSource Document:")

print(doc_names[best_match_index])