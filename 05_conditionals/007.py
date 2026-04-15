# Q87: Check if a number is divisible by both 3 and 5 

number = 18

if number%3 ==0 and number%5==0:
    print("Number is dividbile by both 3 and 5")

elif number%3 ==0:
    print("Number is only divisible by 3")

elif number%5 ==0:
    print("Number is only divisible by 5")

else:
    print("Number is not divisible by both 3 and 5")