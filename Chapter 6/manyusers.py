users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())


#6-7
person_info1 = {'first_name': 'My',
               'last_name': 'Girl',
                'age': 25,
                'city': 'Los Angeles'}
#print(person_info1['first_name'])

person_info2 = {'first_name': 'Dope',
               'last_name': 'Chick',
                'age': 31,
                'city': 'Mexico D.F.'}
#print(person_info2['first_name'])

person_info3 = {'first_name': 'Baby',
               'last_name': 'Girlie',
                'age': 22,
                'city': 'Paris'}
#print(person_info3['first_name'])

#loop through list
person_list = [person_info1, person_info2, person_info3]
for person in person_list:
    print(person)


#6-8 Pet Dictionary to list with loop
pet_info1 = {'animal': 'Cat',
               'owner_name': 'Fany',}
#print(person_info1['first_name'])

pet_info2 = {'animal': 'Dog',
               'owner_name': 'Anthony',}
#print(person_info2['first_name'])

pet_info3 = {'animal': 'Lizard',
               'owner_name': 'Dari',}

pet_list = [pet_info1,pet_info2,pet_info3]

for pet in pet_list:
    print(pet)

favorite_places = {'Anthony': ['Greece', 'Japan'],
                'Dari': 'Mexico',
                'Chester': ['Los Angeles', 'USA', 'Brazil']}


for name, place in favorite_places.items():
    print(name + ": " + str(place))


fav_nums = {'Anthony': [7, 33, 99],
               'Chester': 3,
                'Dari': [25, 63, 64],
                'Girl1': 100,
                'Girl2':[8, 69, 777]}

for name, num in fav_nums.items():
    print(name + "'s favorite number(s) are: " + str(num))

cities = {'Los Angeles': {'Population': 1000000,
                          'Country': 'USA',
                          'Fact': 'Best City in the world'},
            'Mexico DF': {'Population': 500000,
                          'Country': 'Mexico',
                          'Fact': 'Best food in the world'},
            'SAP': {'Population': 10000,
                          'Country': 'Honduras',
                          'Fact': 'Nicest reef in the world'}
          }

cities['New York'] = {'Population': 20000000000,
                          'Country': 'USA',
                          'Fact': 'Best views in the world'}

for city, info in cities.items():
    print(city + " known facts: " + str(info))