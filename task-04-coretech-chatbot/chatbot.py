import pandas as pd

faq = pd.read_csv("coretech_faq.csv")

print("Welcome to CoreTech Chatbot")
print("Type 'exit' to quit")

while True:

    user_question = input("\nYou: ").lower()

    if user_question == "exit":
        print("Chatbot: Thank you for contacting CoreTech.")
        break

    answer_found = False

    for index, row in faq.iterrows():

        faq_question = row["Question"].lower()

        if any(word in faq_question for word in user_question.split()):

            print("Chatbot:", row["Answer"])
            answer_found = True
            break

    if not answer_found:
        print("Chatbot: Sorry, I could not find an answer to that question.")