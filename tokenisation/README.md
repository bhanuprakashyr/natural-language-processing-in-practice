# Tokenisation

## Definition

**Tokenisation** is the process of splitting text into smaller units called **tokens**. These tokens are the building blocks for NLP tasks. Depending on the method, a token can be a word, subword, character, or sentence.

---

## Why It Matters

* Machines cannot directly process raw text.
* Tokenisation defines the **vocabulary** and directly impacts model performance.
* Different tokenisation methods balance vocabulary size vs. ability to handle rare/unknown words.

---

## Types of Tokenisation

### 1. Word Tokenisation

Splits text into words.

```python
from nltk.tokenize import word_tokenize

sentence = "ChatGPT is amazing!"
print(word_tokenize(sentence))
# ['ChatGPT', 'is', 'amazing', '!']
```

### 2. Subword Tokenisation

Breaks words into smaller chunks (subwords) using algorithms like **Byte Pair Encoding (BPE)** or **WordPiece**.

```python
from transformers import BertTokenizer

# Load pretrained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

text = "Tokenisation with BERT is powerful and amazing!"

# Tokenise into subwords
tokens = tokenizer.tokenize(text)
print(tokens)
# ['token', '##isation', 'with', 'bert', 'is', 'powerful', 'and', 'amazing', '!']
```

### 3. Character Tokenisation

Every character is a token.

```python
list("cat")
# ['c', 'a', 't']
```

Useful for morphologically rich languages or handling typos.

### 4. Sentence Tokenisation

Splits text into sentences.

```python
from nltk.tokenize import sent_tokenize

text = "NLP is fun. Tokenisation is key."
print(sent_tokenize(text))
# ['NLP is fun.', 'Tokenisation is key.']
```

---

## Challenges in Tokenisation

* **Ambiguity**: "New York" → one token or two?
* **No spaces**: Languages like Chinese and Japanese require special segmentation.
* **Special tokens**: Emojis, hashtags (#AI), URLs, mentions (@user).

---

## Common Tokenisation Libraries

### 1. NLTK

* Classic library for tokenisation and basic NLP tasks.
* Functions: `word_tokenize()`, `sent_tokenize()`.

### 2. spaCy

* Fast, production-ready NLP library.

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Tokenisation with spaCy is fast!")
print([token.text for token in doc])
# ['Tokenisation', 'with', 'spaCy', 'is', 'fast', '!']
```

### 3. Hugging Face `tokenizers`

* High-performance, used in modern Transformer models.

```python
from tokenizers import Tokenizer

# Example with pretrained model
tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
output = tokenizer.encode("HuggingFace makes NLP easy.")
print(output.tokens)
```

### 4. SentencePiece (Google)

* Unsupervised, whitespace-agnostic, great for Asian languages.

```python
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load("m.model")
print(sp.encode_as_pieces("SentencePiece handles subwords!"))
```

### 5. Moses Tokeniser

* Older tokenizer, designed for machine translation.
* Still used in MT research (fairseq, WMT benchmarks).

### 6. Gensim

* Simple preprocessing utilities.

```python
from gensim.utils import simple_preprocess
print(simple_preprocess("Gensim simplifies tokenisation!"))
# ['gensim', 'simplifies', 'tokenisation']
```

---

## Key Points

* Tokenisation is the **first step** in most NLP pipelines.
* Choice of tokenisation method affects vocabulary size, efficiency, and performance.
* Modern NLP relies on **subword tokenisation** to balance efficiency and generalisation.

