# Q118: Count frequency of each character in a string 

text = "hello"
frequency = {}
count = 0

for char in text:
    if char in frequency:
        frequency[char] = frequency[char]+1

    else:
        frequency[char] =1

print(frequency)

