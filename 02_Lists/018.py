# Find common elements between two lists

list1 = [1, 2, 3, 4, 5,7] 
list2 = [4, 5, 6, 7, 8]

common_elements = []

for item_1 in list1:
    for item_2 in list2:
        if item_1 == item_2:
            common_elements.append(item_2)
            
print(common_elements)


# Shortcut
common = list(set(list1) & set(list2))

print(common)