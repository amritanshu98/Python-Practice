# Q61: Get the key with maximum value in a dictionary 

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

max_value = 0

for keys, values in scores.items():
    if values> max_value:
        max_value = values

print(max_value)


# Shortcut
# max_value = max(scores.values())
# print(max_value)