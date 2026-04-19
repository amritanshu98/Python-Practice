# Q108: Print all even numbers from 1 to 100 using a loop 

n = 100
even_num = []

for i in range(1, n+1):
    if i%2 ==0:
        even_num.append(i)

print(even_num)