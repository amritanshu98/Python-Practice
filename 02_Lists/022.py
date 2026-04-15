#  Find union of two lists

list1 = [1, 2, 3, 4, 4] 
list2 = [4, 5, 6, 6, 7] 

new_list = list(set(list1) | set(list2))

print(new_list)