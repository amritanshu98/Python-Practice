# Sort a list of numbers 

numbers = [5, 2, 8, 1, 9, 3]
sorted_nums = []

while len(numbers) >0:
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        
    sorted_nums.append(smallest)
    numbers.remove(smallest)


print(sorted_nums)









# Shortcut
# sorted_nums = sorted(numbers)

# print(sorted_nums)