# Q63: Find keys in a dictionary that have a specific value 

person = {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'} 
search_value = 25

for keys, values in person.items():
    if search_value==values:
        print(keys)