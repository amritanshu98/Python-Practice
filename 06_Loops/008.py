# Q103: Find reverse of a number using a loop 

number = 12345

# reversed_num = int(str(number)[::-1])


# print(reversed_num)
# print(type(reversed_num))

reverse = 0 

while number> 0:
    last_digit = number %10
    reverse = reverse*10+last_digit
    number = number//10

print(reverse)


