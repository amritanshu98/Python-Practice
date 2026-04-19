# Write a program which can compute the factorial of a given number. Suppose the input is 8, then the output should be 40320.

num = 8

fact = 1

for i in range(1,num+1):
    fact = fact*i

print(fact)