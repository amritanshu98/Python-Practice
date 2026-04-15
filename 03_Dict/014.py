# Q59: Calculate sum of values in a dictionary 

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95} 

sum_scores = 0

for keys,values in scores.items():
    sum_scores = sum_scores+values
    
print(sum_scores)


#Shortcut
total = sum(scores.values())
print(total)