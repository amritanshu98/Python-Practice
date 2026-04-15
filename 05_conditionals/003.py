# Q83: Check if a year is a leap year 

# Leap year rules: 
# 1. Divisible by 4 
# 2. If divisible by 100, must also be divisible by 400 
 

year = 2024

if year%4==0:
    if year%100 !=0  or year%400==0:
        print("Leap Year")

else:
    print("Not a Leap Year")