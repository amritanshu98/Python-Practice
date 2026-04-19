# Q104: Count number of digits in a number using a loop

number = 12345

string = str(number)

length = 0

# for i in string:
#     length +=1

while number>0:
    last_digit = number%10
    length +=1
    number = number//10


print(length)
