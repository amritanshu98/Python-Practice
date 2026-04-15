# Q50: Merge two dictionaries 

dict1 = {'a': 1, 'b': 2} 
dict2 = {'c': 3, 'd': 4}

# new_dict = dict1 | dict2

# new_dict = {}

# for key,value in dict1.items():
#     new_dict[key]=value

# for key,value in dict2.items():
#     new_dict[key]=value

# print(new_dict)

up_dict = dict1.copy()

up_dict.update(dict2)

print(up_dict)