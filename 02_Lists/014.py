#  Count number of even and odd numbers in a list 

list = [1,2,3,4,5,6,7,8,9,10,11]


count_even = 0
count_odd = 0

for num in list:
    if num%2 ==0:
        count_even +=1
    
    else:
        count_odd +=1

print(count_even)
print(count_odd)

