# Q28: Merge two sorted lists 

from hmac import new


list1 = [1, 3, 5, 7] 
list2 = [2, 4, 6, 8] 


i = 0
j = 0

new_list = []

while i < len(list1) and j < len(list2):
    if list1[i]< list2[j]:
        new_list.append(list1[i])
        i +=1

    else: 
        new_list.append(list2[j])
        j +=1

while i< len(list1):
    new_list.append(list1[i])
    i +=1

while j< len(list2):
    new_list.append(list2[j])
    j +=1

print(new_list)







# Shortcut
# new_list = list(list1+list2)

# new_list.sort()

# print(new_list)