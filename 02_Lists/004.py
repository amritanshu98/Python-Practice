# Q24: Remove duplicates from a list 

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]



new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)


print(new_list)



# Shortcut
# new_list = set(numbers)

# print(new_list)