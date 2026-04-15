# Q43: Check if two lists are identical 
 
# Input 
list1 = [1, 2, 3, 4, 5] 
list2 = [1, 2, 3, 4, 5] 
list3 = [1, 2, 3, 4, 3] 

if list1 == list2 == list3:
    print("List 1 & 2 & 3 are identical")

elif list1 == list2:
    print("List 1 & 2 are identical")

elif list1 == list3:
    print("List 1 & 3 are identical")

elif list2 == list3:
    print("List 2 & 3 are identical")

else:
    print("Lists are not identical")