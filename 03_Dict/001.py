# Q46: Create dictionary from two lists (keys and values) 

keys = ['name', 'age', 'city'] 
values = ['Alice', 25, 'New York']
dict_1 = {}

for i in range(len(keys)):
    dict_1[keys[i]] = values[i]

print(dict_1)

# Shortcut

dict_2 =  dict(zip(keys, values)) 

print(dict_2)
