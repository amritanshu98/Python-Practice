# Reverse the order of words in a string

sentence = "Hello World from Python"

words = sentence.split()

rev_sentence = " ".join(words[::-1])

print(rev_sentence)