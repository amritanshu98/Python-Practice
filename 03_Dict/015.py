# Q60: Remove all duplicate values from a dictionary 
 
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}
new_dict = {}
seen = []

for keys, values in data.items():
    if values not in seen:
        new_dict[keys] = values
        seen.append(values)

print(new_dict)


# data_values = list(set(data.values()))

# print(data_values)

# unique_values_dict = {} 
# seen_values = set() 

# for key, value in data.items():
#     if value not in seen_values:
#         unique_values_dict[key] = value
#         seen_values.add(value)

# print(unique_values_dict)