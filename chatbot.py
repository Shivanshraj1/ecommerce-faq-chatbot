from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import load_faqs, preprocess_faqs, preprocess_text


class FAQChatbot:
    def __init__(self, similarity_threshold=0.2):
        self.similarity_threshold = similarity_threshold
        self.faqs = preprocess_faqs(load_faqs())
        self.vectorizer = TfidfVectorizer()

        questions = [faq["processed_question"] for faq in self.faqs]
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def get_response(self, user_question):
        processed_question = preprocess_text(user_question)
        user_vector = self.vectorizer.transform([processed_question])

        similarities = cosine_similarity(user_vector, self.question_vectors).flatten()
        best_match_index = similarities.argmax()
        best_score = similarities[best_match_index]
        best_faq = self.faqs[best_match_index]

        if best_score < self.similarity_threshold:
            return {
                "answer": "Sorry, I could not find a suitable answer. Please rephrase your question.",
                "matched_question": None,
                "score": round(float(best_score), 3),
                "category": None,
            }

        return {
            "answer": best_faq["answer"],
            "matched_question": best_faq["question"],
            "score": round(float(best_score), 3),
            "category": best_faq["category"],
        }


def main():
    chatbot = FAQChatbot()

    print("E-commerce FAQ Chatbot")
    print("Type 'exit' to stop.\n")

    while True:
        user_question = input("You: ").strip()

        if user_question.lower() in {"exit", "quit", "bye"}:
            print("Bot: Thank you for chatting!")
            break

        if not user_question:
            print("Bot: Please enter a question.")
            continue

        response = chatbot.get_response(user_question)
        print(f"Bot: {response['answer']}")
        print(f"Matched FAQ: {response['matched_question']}")
        print(f"Similarity score: {response['score']}\n")


if __name__ == "__main__":
    main()
