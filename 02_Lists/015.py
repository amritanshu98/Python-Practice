# Q35: Flatten a nested list

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

single_list = []

for items in nested_list:
    for item in items:
        single_list.append(item)


# Shortcut

# single_list = sum(nested_list, [])

print(single_list)