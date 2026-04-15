#  Update the value of a key in a dictionary

person = {'name': 'Alice', 'age': 25, 'city': 'New York'} 

person['age'] = 30

print(person)

person.update({'city': 'California'})

print(person)

# Adding New Element
person['country'] = "USA"

print(person)