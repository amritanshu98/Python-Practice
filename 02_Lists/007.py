#  Find second largest number in a list 


numbers = [10, 20, 4, 45, 99, 99, 50]


max_num = float('-inf')
second_max = float('-inf')

for num in numbers:
    if num > max_num:
        second_max = max_num
        max_num = num

    elif num>second_max and num != max_num:
        second_max = num

print(second_max)





# Shortcut:

# new_list = list(set(numbers))
# new_list.sort()

# print(new_list)
# print(f"Second Largest Number: {new_list[-2]}")
