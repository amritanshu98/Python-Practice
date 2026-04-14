# Q1: Write a program to check if a string is a palindrome

word = "madama"

rev_word = word[::-1]

print(rev_word)

if word == rev_word:
    print(f"{word} is Palindrome")

else:
    print(f"{word} is not Palindrome")



