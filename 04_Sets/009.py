# Q74: Find symmetric difference of two sets 

set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8} 

intersection = set1 & set2

union = set1 | set2

# symmetric_set = union.difference(intersection)

symmetric_set = set1.symmetric_difference(set2)

print(symmetric_set)