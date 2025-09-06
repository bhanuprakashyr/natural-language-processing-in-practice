# NLP Key Definitions

1. **Natural Language Processing (NLP)**
   Natural Language Processing (NLP) is a field of Artificial Intelligence that enables machines to understand, interpret, and generate human language. It combines computational linguistics, machine learning, and deep learning to process text and speech data.
   **Example:** Sentiment analysis, chatbots, translation.

---

2. **Corpus**
   A corpus is just a large, structured collection of texts used for training or analyzing language models. Think of it as your "data universe."
   **Example:** Wikipedia dump, news articles, or tweets.
   **Plural:** corpora.
   In modern NLP, corpora are often preprocessed into clean, machine-readable form.

---

3. **Token**
   A token is the smallest unit of text a model works with (word, subword, character, or punctuation).
   **Example:** "Cats are running." → Tokens: \["Cats", "are", "running", "."]

---

4. **Vocabulary**
   Vocabulary is the set of all unique tokens in a corpus.
   **Example:** If a corpus contains only {"dog", "dogs", "run", "runs"}, the vocabulary size = 4.

---

5. **Lemmatization vs. Stemming**

* **Stemming:** Roughly cuts word endings to get a base form. ("running" → "run", "flies" → "fli").
* **Lemmatization:** Uses linguistic rules to return the true root word. ("running" → "run", "flies" → "fly").

---

6. **Feature Extraction**
   The process of transforming raw text into useful features (numeric or categorical) that a machine learning model can use. This can include vectorisation, sentiment scores, or syntactic tags.
   **Example:** Bag-of-Words, TF-IDF.

---

7. **Vectorisation**
   Vectorisation is a specific type of feature extraction that represents text as numerical vectors.
   **Example methods:** One-hot encoding, Bag-of-Words, TF-IDF, embeddings (Word2Vec, GloVe, BERT).

---

8. **Named Entity Recognition (NER)**
   NER identifies proper nouns in text and classifies them into predefined categories.
   **Example:** "Barack Obama was born in Hawaii." → \[Barack Obama → PERSON], \[Hawaii → LOCATION].

---

9. **Sentiment Analysis**
   Sentiment analysis classifies text based on emotional tone.
   **Example:** "This phone is amazing!" → Positive sentiment.

---

10. **Embedding**
    An embedding is a dense, low-dimensional vector representation of words or documents that captures semantic meaning.
    **Example:** Word2Vec analogy → king – man + woman ≈ queen.
