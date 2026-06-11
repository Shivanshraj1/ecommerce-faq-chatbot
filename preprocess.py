import csv
import re
from pathlib import Path

from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize


DATA_PATH = Path(__file__).parent / "data" / "faqs.csv"

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "can",
    "do",
    "for",
    "from",
    "how",
    "i",
    "if",
    "in",
    "is",
    "it",
    "my",
    "of",
    "on",
    "or",
    "the",
    "to",
    "what",
    "when",
    "where",
    "which",
    "why",
    "with",
    "you",
    "your",
}

stemmer = PorterStemmer()


def load_faqs(csv_path=DATA_PATH):
    """Load FAQ records from the CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def preprocess_text(text):
    """Clean, tokenize, remove stop words, and stem text."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", " ", text)

    tokens = wordpunct_tokenize(text)
    cleaned_tokens = [
        stemmer.stem(token)
        for token in tokens
        if token.isalnum() and token not in STOP_WORDS
    ]

    return " ".join(cleaned_tokens)


def preprocess_faqs(faqs):
    """Add a preprocessed question field to each FAQ record."""
    processed = []

    for faq in faqs:
        processed.append(
            {
                **faq,
                "processed_question": preprocess_text(faq["question"]),
            }
        )

    return processed


if __name__ == "__main__":
    faqs = load_faqs()
    processed_faqs = preprocess_faqs(faqs)

    print(f"Loaded FAQs: {len(processed_faqs)}")
    print("\nSample preprocessing:")

    for faq in processed_faqs[:5]:
        print(f"Original : {faq['question']}")
        print(f"Processed: {faq['processed_question']}\n")
