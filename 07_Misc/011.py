# Accept a sentence and count the number of letters and digits separately. E.g. 'hello world! 123' → LETTERS 10, DIGITS 3

inp = "hello world! 123"
alpha_count = 0
digit_count = 0
other_count = 0

for char in inp:
    if char.isalpha():
        alpha_count +=1
    
    elif char.isdigit():
        digit_count +=1

    else:
        other_count +=1

print(f"Alphabet Count: {alpha_count}")
print(f"Digit Count: {digit_count}")
print(f"Other Character Count: {other_count}")

