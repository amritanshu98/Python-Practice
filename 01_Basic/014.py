# Find the longest word in a string 

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()

longest_word = ""
longest_length = 0

for word in words:
    if len(word)> longest_length:
        longest_word = word
        longest_length = len(word)

print(f"longest word: {longest_word} with length {longest_length}")


