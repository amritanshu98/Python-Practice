# Q30: Concatenate two lists

from hmac import new


list_1 = [1,2,3,4,5]

list_2 = [6,7,8,9,0]

new_list = []

for nums in list_1:
    new_list.append(nums)

for nums in list_2:
    new_list.append(nums)


# new_list = list_1+list_2


print(new_list)
