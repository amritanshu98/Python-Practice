#  Replace all occurrences of a substring

from operator import ne


text = "I like apples, apples are tasty."

old_word = "apples"
new_word = "mangoes"

result = text.lower().replace(old_word, new_word)
print(result)
