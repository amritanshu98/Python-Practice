# Accept a sentence and separately count uppercase and lowercase letters. E.g. 'Hello world!' → UPPER CASE 1, LOWER CASE 9.

inp = "Hello World"

uppercase_count = 0
lowercase_count = 0
other_count = 0

for char in inp:
    if char.isupper():
        uppercase_count +=1
    elif char.islower():
        lowercase_count +=1
    else:
        other_count +=1

print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
print(f"Other Letters: {other_count}")




