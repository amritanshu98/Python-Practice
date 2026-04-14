    #  Write a program to count words in a string

word = "Python Program"
list = []

for char in word:
    list.append(char)

print(list)
print(f"Count of words in list: {len(list)}")




#Words Count
count_wrd = word.split()

print(len(count_wrd))