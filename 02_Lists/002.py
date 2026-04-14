# Reverse a list without using built-in functions

list = [1,2,3,4,5,6,7,8,9]
rev_list = []

for num in range(len(list)-1, -1, -1):
    rev_list.append(list[num])

print(rev_list)


# Shortcut
rev_list_1 = list[::-1]

print(rev_list_1)

