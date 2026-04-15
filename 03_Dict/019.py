# Q64: Group elements in a list by frequency using a dictionary 

numbers = [1,1, 2, 3, 3, 3,3, 4, 4, 4, 4,4,5,5]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num]+1

    else:
        frequency[num] =1

print(frequency)