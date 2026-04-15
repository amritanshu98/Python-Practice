# Q56: Get a list of all keys and values in a dictionary 
 
person = {'name': 'Alice', 'age': 25, 'city': 'New York'} 

key_list = []
value_list = []

for keys,values in person.items():
    key_list.append(keys)
    value_list.append(values)

print(key_list)
print(value_list)


keys_list = list(person.keys()) 
values_list = list(person.values()) 

print(keys_list)
print(values_list)

