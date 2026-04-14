# Find maximum and minimum elements in a list 

list = [12, 45, 77, 87, 35, 6, 57, 29]

max_num = list[0]
min_num = list[0]

for num in list:
    if num> max_num:
        max_num = num
    
    if num< min_num:
        min_num = num

print(f"Maximum Num: {max_num}")
print(f"Mininum Num: {min_num}")


# Direct using min-max function

print(max(list))
print(min(list))

