# Write a program to reverse a string 

# text = "abcdefg"

# rev_text = text[::-1]

# print(rev_text)

#from slicing

word = "Python"
rev_word = ""

for i in range(len(word)-1, -1, -1):
    rev_word = rev_word + word[i]

print(rev_word)