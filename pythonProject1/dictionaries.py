personal: dict[str, object] = {'f_name': "Reuben", 'l_name': "Herrera",
                               "age": 39, "smoker": True, 'siblings': [26, 30, 42],
                               'address': {
                                   'city': 'Hadera',
                                   'street': 'Ben yehuda',
                                   'number': 10,
                                   'zipcode': 30210
                               }}

# 1 fill the data -

print(personal)

# 2 get the age value using  [ ], and using get function

print(personal['age'])
print(personal.get('age'))

# 3 change the smoker to False

personal["smoker"] = False
print(personal)

# 4 del key-value l_name

del personal['l_name']
print(personal)

# 5 get first age of siblings

print(personal.get('siblings', [0])[0])

# 6 get zip code

print(personal.get('address', {}.get('zipcode')))
print(personal)

# 7 update the address.number with same value + 1

personal ['address']['number'] += 1
print(personal)

# 8 del adress.zipcode

del personal['address'] ['zipcode']

# print the new dict
print(personal)