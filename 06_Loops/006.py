# Q101: Print all prime numbers between 1 and 100 using a loop 

n = 100
prime_num = []


for num in range(1, n+1):
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num%i ==0:
                break
        else:
            prime_num.append(num)


print(prime_num)
            