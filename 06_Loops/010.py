# Q105: Find sum of digits of a number using a loop 

number = 12345
sum = 0

while number > 0:
    last_digit = number%10
    sum = sum+last_digit
    number = number//10

print(sum)