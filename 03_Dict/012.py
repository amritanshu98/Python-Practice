# Q57: Sort a dictionary by its keys 

scores = {'Bob': 85, 'Alice': 92, 'Charlie': 78, 'Diana': 95}

# new_dict = dict(sorted(scores.items()))

new_dict = {}

sorted_keys = sorted(scores.keys())

for keys in sorted_keys:
    new_dict[keys] = scores[keys]




print(new_dict)