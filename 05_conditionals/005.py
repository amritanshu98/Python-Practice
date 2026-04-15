# Q85: Check if a string contains a vowel 
 
from pydantic import conset


text = "Hello World"

vowels = "aeiouAEIOU"
vowel_count = 0
consonsnt_count = 0
found = False

for char in text:
    if char in vowels:
        found = True
        break

if found:
    print('Yes Vowels is present')

else:
    print("No Vowels present")

# for char in text:
#     if char in vowels:
#         vowel_count +=1
    
#     else:
#         consonsnt_count +=1

# print(vowel_count)
# print(consonsnt_count)
