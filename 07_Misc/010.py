# Find all numbers between 1000 and 3000 (both included) where each digit of the number is an even number (0, 2, 4, 6, 8). Print in comma-separated form.

result = []

for num in range(1000, 3001):
    num_str = str(num)

    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num_str)

print(",".join(result))