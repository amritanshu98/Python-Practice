# Q100: Count number of even numbers in a list using a loop 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for num in numbers:
    if num%2 ==0:
        count +=1

print(count)