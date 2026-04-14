# Q17: Remove duplicate characters from a string

input_string = "programming"

result = ""

new_set = set()

for char in input_string:
    if char not in new_set:
        new_set.add(char)
        result += char


print(input_string)
print(result)


