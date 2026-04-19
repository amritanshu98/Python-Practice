# Q106: Reverse a list using a loop 

my_list = [1, 2, 3, 4, 5] 

new_list = []

for i in range(len(my_list)-1, -1, -1):
    new_list.append(my_list[i])

print(new_list)
