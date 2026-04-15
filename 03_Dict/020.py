# Q65: Sort a dictionary by its values 

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}

new_dict = dict(sorted(scores.items(), key=lambda item: item[1]))

print(new_dict)


