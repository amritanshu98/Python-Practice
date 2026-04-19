# Accept a comma-separated sequence of words and print them sorted alphabetically. E.g. input: without,hello,bag,world → output: bag,hello,without,world.


input= ["without","hello","bag","world"]

words = sorted(input)
print(words)

for word in words:
    print(word, end=",")