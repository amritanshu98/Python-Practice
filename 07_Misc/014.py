# Use a list comprehension to filter only odd numbers from a comma-separated input list. E.g. 1,2,3,4,5,6,7,8,9 → 1,3,5,7,9.

inp = [1,2,3,4,5,6,7,8,9]

for num in inp:
    if num%2!=0:
        print(num, end=",")




