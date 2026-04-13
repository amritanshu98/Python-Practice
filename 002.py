# Q2: Write a program to count vowels and consonants


text = "Hello World"

vowel_count = 0
consonants_count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count = vowel_count+1

        else: 
            consonants_count = consonants_count+1

print(f"vowel count: {vowel_count}")
print(f"consonants count: {consonants_count}")