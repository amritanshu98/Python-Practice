# Rotate a list by specified number of positions 

my_list = [1, 2, 3, 4, 5] 
k = 2  # Rotate by 2 positions 

rotated_list = []

n = len(my_list)

for i in range(n):
    rotated_list.append(my_list[(i-k)%n])

print(rotated_list)