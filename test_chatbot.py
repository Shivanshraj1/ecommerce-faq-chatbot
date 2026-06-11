from chatbot import FAQChatbot


TEST_QUESTIONS = [
    "Where is my package?",
    "I want to cancel my purchase.",
    "My payment was deducted but no order is showing.",
    "How can I return a damaged item?",
    "I forgot my password.",
    "Do you ship to other countries?",
    "Can I pay when the product arrives?",
    "How do I know if this item is available?",
    "Can I exchange my product?",
    "What is the weather today?",
]


def main():
    chatbot = FAQChatbot()

    print("FAQ Chatbot Test Results")
    print("=" * 60)

    for question in TEST_QUESTIONS:
        response = chatbot.get_response(question)

        print(f"User question   : {question}")
        print(f"Matched question: {response['matched_question']}")
        print(f"Category        : {response['category']}")
        print(f"Score           : {response['score']}")
        print(f"Bot answer      : {response['answer']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
