# Q58: Find common keys between two dictionaries 
# python 
# # Input 
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
dict2 = {'b': 20, 'c': 30, 'e': 50, 'f': 60} 

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print(common_keys)


# list_1 = []

# list_2 =[]

# for key in dict1:
#     list_1.append(key)

# for key in dict2:
#     list_2.append(key)


# # print(list_1)
# # print(list_2)

# common_keys = []

# for i in list_1:
#     for j in list_2:
#         if i==j:
#             common_keys.append(i)

# print(common_keys)


# Sfortcut
# common_keys = set(dict1.keys()) & set(dict2.keys())

# print(common_keys)





