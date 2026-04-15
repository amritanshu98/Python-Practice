# Q73: Convert a list into a set and remove duplicates 

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5] 

new_set = set()

for i in my_list:
    new_set.add(i)

print(new_set)

new_set_1 = set(my_list)
print(new_set)