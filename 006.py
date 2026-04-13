# Q6: Remove all whitespaces from a string 

from re import split


text = "Hello World Python Programming"

# text_1 =text.replace(" ", "")

text_1 = "".join(text.split())

print(text_1)
