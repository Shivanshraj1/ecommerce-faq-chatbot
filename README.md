# E-commerce FAQ Chatbot

This internship project builds a chatbot that answers common e-commerce customer-support questions by matching a user's message with the most similar question in an FAQ dataset.

## Step 2: FAQ Dataset

The starter dataset is stored in `data/faqs.csv`. It contains 30 question-and-answer pairs across these categories:

- Orders
- Shipping
- Payments
- Returns
- Refunds
- Accounts
- Products

Each record contains an `id`, `category`, `question`, and `answer`. Later steps will preprocess the questions and use TF-IDF with cosine similarity to find the best response.

## Step 3: Text Preprocessing

The `preprocess.py` file loads the FAQ CSV and prepares question text for similarity matching.

It performs:

- Lowercasing
- Punctuation removal
- Tokenization using NLTK
- Stop-word removal
- Stemming using NLTK's `PorterStemmer`

Run it with:

```bash
python preprocess.py
```

## Step 4: FAQ Matching

The `chatbot.py` file matches a user's question with the most similar FAQ question.

It uses:

- `TfidfVectorizer` from scikit-learn to convert text into numerical vectors
- `cosine_similarity` to compare the user question with every FAQ question
- A similarity threshold so the bot can avoid giving weak or unrelated answers

Run it with:

```bash
python chatbot.py
```

Example:

```text
You: Where is my package?
Bot: Open My Orders and select Track Package. You will also receive a tracking link by email or SMS after shipment.
Matched FAQ: How can I track my package?
Similarity score: 0.59
```

## Step 5: Testing

The `test_chatbot.py` file runs the chatbot against sample customer questions.

Run:

```bash
python test_chatbot.py
```

This helps check whether the chatbot is matching user questions with the correct FAQ. It also includes one unrelated question so you can show how the threshold handles unknown queries.

## Step 6: Chat UI

The `app.py` file provides a simple Streamlit chat interface.

Run:

```bash
streamlit run app.py
```

The UI lets users type questions, view chatbot answers, and open match details to see the matched FAQ, category, and similarity score.
