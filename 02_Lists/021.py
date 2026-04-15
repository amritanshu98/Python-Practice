# Find intersection of two lists
list1 = [1, 2, 3, 4, 5, 4] 
list2 = [4, 5, 6, 7, 8, 4]

new_list = []

temp_list = list2.copy()



for item in list1:
    if item in temp_list:
            new_list.append(item)
            temp_list.remove(item)

print(new_list) # Contains Duplicate


# Shortcut

new_list2 = list(set(list1) & set(list2))


print(new_list2)

