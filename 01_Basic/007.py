# Check if two strings are anagrams 

text_1 = "Listen"
text_2 = "Silent"

if sorted(text_1.lower()) == sorted(text_2.lower()):
    print("Yes Anagram")
else:
    print("Not Anagram")