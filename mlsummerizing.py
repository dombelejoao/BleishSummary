import nltk
nltk.download('punkt')
from collections import Counter
import numpy as np

nltk.download('punkt')

def luhn_summarization(text, num_sentences=3):
    sentences = nltk.sent_tokenize(text)
    
    words = nltk.word_tokenize(text.lower())
    word_freq = Counter(words)
    
    significant_words = {word: freq for word, freq in word_freq.items() if 1 < freq < 0.05 * len(words)}
    
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = nltk.word_tokenize(sentence.lower())
        score = sum(significant_words.get(word, 0) for word in sentence_words)
        sentence_scores[sentence] = score
    
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return ' '.join(summarized_sentences)

if __name__ == "__main__":
    with open("blog_post.txt", "r") as file:
        blog_post_text = file.read()

summary = luhn_summarization(blog_post_text)
print(summary)