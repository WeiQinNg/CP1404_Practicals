"""
CP1404/CP5632 Practical 5
Word occurences
Program to count the occurrences of words in a string
Estimate: 25 minutes
Actual:    minutes
"""

text = input(f"Text: ")
words = text.split()
words.sort()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

width = max(len(word) for word in word_to_count)
for word in word_to_count:
    print(f"{word:{width}} : {word_to_count[word]}")
