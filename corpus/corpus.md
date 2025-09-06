# Corpus

## Definition

A **corpus** is a large, structured collection of texts used for training or analyzing language models. Think of it as your **data universe** in NLP.

* **Plural:** corpora
* In modern NLP, corpora are often preprocessed into clean, machine-readable form before use.

---

## Examples

* Wikipedia dumps
* News articles
* Tweets
* Research papers

---

## Why It Matters

* Provides the raw material for building NLP models.
* Quality and diversity of a corpus directly affect model performance.
* Specialized corpora exist for domains (e.g., medical, legal, social media).

---

## Commonly Used Corpora in NLP

* **Brown Corpus**: First million-word electronic corpus of English.
* **Penn Treebank**: Annotated corpus with syntactic and semantic info.
* **IMDB Reviews**: Popular for sentiment analysis.
* **COCO Captions**: Image descriptions for multimodal NLP tasks.

---

## Preprocessing of Corpora

Not all corpora in NLTK (or elsewhere) are preprocessed. Some come raw, others are tokenised or even annotated.

### How to Identify

* If the corpus has `.words()` or `.sents()`, it’s already **tokenised**.
* If the corpus has `.raw()`, it’s in **raw text form**.
* If the corpus has `.tagged_words()` or `.parsed_sents()`, it’s **preprocessed & annotated**.

### Quick Reference Table (NLTK)

| Corpus            | Preprocessed? | Notes                                                        |
| ----------------- | ------------- | ------------------------------------------------------------ |
| **Brown**         | ✔ Tokenised   | Provides `.words()`, `.sents()`, and `.tagged_words()`       |
| **Gutenberg**     | ✘ Raw text    | Use `.raw()`, must tokenize manually                         |
| **Treebank**      | ✔✔ Annotated  | Tokenised + POS tagged + parsed                              |
| **Movie Reviews** | Partial       | Pre-split into pos/neg categories, but requires tokenisation |

---

## Key Points

* A corpus is the foundation of any NLP pipeline.
* Needs preprocessing (tokenisation, stopword removal, etc.) if raw.
* Different corpora suit different tasks.
