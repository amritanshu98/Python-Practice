# Accept space-separated words, remove all duplicates, and print them sorted alphanumerically. E.g. 'hello world and practice makes perfect and hello world again' → 'again and hello makes perfect practice world'.

words = "hello world and practice makes perfect and hello world again"

list_new = words.split()

result = sorted(set(list_new))

print(" ".join(result))

