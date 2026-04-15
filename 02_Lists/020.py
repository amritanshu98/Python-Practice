# Q40: Find cumulative sum of elements in a list

numbers = [1, 2, 3, 4, 5]

cumulative = []
sum =0

for num in numbers:
    sum = sum+num
    cumulative.append(sum)

print(cumulative)
