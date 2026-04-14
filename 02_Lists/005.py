#  Count occurrences of an element in a list 

numbers = [1, 2, 3, 2, 4, 2, 5, 3, 1, 1, 1, 1, 1]

# for all numbers: 
element = {}

for num in numbers:
    if num in element:
        element[num] +=1
    
    else:
        element[num] =1

print(element)


# for single number:
element_1 =1
count = 0

for num in numbers:
    if num == element_1:
        count = count+1

print(count)



# Shortcut
# print(numbers.count(1))

# print(countOf(numbers, 1))



    


