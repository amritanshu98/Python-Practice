# Q116: Check if a string is a valid palindrome (ignoring spaces and case) 

text = "A man a plan a canal panama" 

new_text = text.lower().replace(" ", "")

revrese = new_text[::-1]

if new_text == revrese:
    print("Yes Palindrome")

else:
    print("Not a Palindrome")
