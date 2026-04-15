# Q62: Filter dictionary entries based on their values 

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88} 
# Filter: keep entries with value >= 85
threshold = 85

new_dict = {}

for keys, values in scores.items():
    if values>= threshold:
        new_dict[keys] = values


print(new_dict)



