# Split a list into even and odd numbers

from typing import OrderedDict


list = [2,3,4,5,6,7,8,9]

even_num = []

odd_num =[]

for nums in list:
    if nums %2 ==0:
        even_num.append(nums)

    else:
        odd_num.append(nums)

print(even_num)
print(odd_num)