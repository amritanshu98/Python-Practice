#  Count occurrences of a character in a string

text = "hello world"

char_count = "l"

count = 0

for char in text:
    if char == char_count:
        count = count+1

print(f"count of {char_count}: {count}")


# for all words

mpp = {}

for char in text:
    if char in mpp:
        mpp[char] += 1

    else:
        mpp[char]= 1

print(mpp)