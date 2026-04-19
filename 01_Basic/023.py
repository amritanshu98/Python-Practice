# Q119: Find first non-repeating character in a string 

text = "swiss"
list = []

for char in text:
    if char not in list:
        print(char)

