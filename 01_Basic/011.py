#  Find index of first occurrence of a substring

text = "Hello world, welcome to Python"
substring = "worlds"

index = text.find(substring)

if index !=-1:
    print(f"{substring} found at index: {index}")

else:
    print(f"{substring} not found.")

print(index)




