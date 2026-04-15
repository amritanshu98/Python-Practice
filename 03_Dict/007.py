# Q52: Count frequency of each word in a string using dictionary 
from typing import Counter

 

text = "the quick brown fox jumps over the lazy dog the fox"

words = text.lower().split()

word_count = {}

for word in words: 
    if word in word_count: 
        word_count[word] = word_count[word] + 1 

    else: 
        word_count[word] = 1 

for word, count in word_count.items(): 
    print(f"  '{word}': {count}")



# print(words)

# Shrotcut
# word_count2 = Counter(words) 
# print(word_count2)

