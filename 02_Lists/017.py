# Q37: Remove all occurrences of a value from a list 


numbers = [1, 2, 3, 2, 4, 2, 5] 
value_to_remove = 2 
new_list = []

for num in numbers:
    if num != value_to_remove:
        new_list.append(num)

print(new_list)
