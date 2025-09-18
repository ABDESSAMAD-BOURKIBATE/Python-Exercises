import re

paragraph = """
Python is a powerful programming language. It is widely used in data science, web development, and automation. 
Many developers enjoy its simplicity and readability.
"""

characters = len(paragraph)
sentences = len(re.findall(r'[.!?]', paragraph))
words = paragraph.split()
word_count = len(words)
unique_words = set(words)
unique_word_count = len(unique_words)
non_whitespace = len(paragraph.replace(" ", "").replace("\n", ""))
avg_words_per_sentence = word_count / sentences
non_unique_words = word_count - unique_word_count

print(" Text Analysis Report")
print("------------------------")
print(f"Characters: {characters}")
print(f"Sentences: {sentences}")
print(f"Words: {word_count}")
print(f"Unique words: {unique_word_count}")
print(f"Non-whitespace characters: {non_whitespace}")
print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
print(f"Non-unique words: {non_unique_words}")