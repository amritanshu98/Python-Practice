# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included), and then print the dictionary. If n=8, output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

num = 8

sqr_dict = {}

for i in range(1, num+1):
    sqr_dict[i] = i*i

print(sqr_dict)