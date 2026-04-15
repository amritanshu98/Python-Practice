# Q51: Find maximum and minimum value in a dictionary 

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
max_value = float('-inf')
min_value= float('inf')

max_value_key = None
min_value_key = None

for key,value in scores.items():
    if value>max_value:
        max_value = value
        max_value_key = key

    if value <  min_value:
        min_value = value
        min_value_key = key

print(max_value)

print(min_value)

max = max(scores.values())
print(max)
min = min(scores.values())
print(min)