# Q53: Check if a key exists in a dictionary 

person = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
key_to_check = 'age' 

found = False

# if key_to_check in person:
#     print("Available")

# else:
#     print("Not Available")

for keys, values in person.items():
    if keys == key_to_check:
        found = True
        break
if found:
    print("Available")

else:
    print("Not Available")