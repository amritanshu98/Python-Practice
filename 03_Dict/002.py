# Access a value by key in a dictionary 

person = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
key = 'name'

# value = person[key]
value = person.get(key)


print(value)