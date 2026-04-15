# Q55: Invert a dictionary (swap keys and values) 

original = {'a': 1, 'b': 2, 'c': 3} 

new_dict = {}

for keys, values in original.items():
    new_dict[values] = keys

print(new_dict)