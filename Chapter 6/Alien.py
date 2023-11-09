alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
   # Move the alien to the right.
# Determine how far to move the alien based on its current speed. u
if alien_0['speed'] == 'slow':
       x_increment = 1
elif alien_0['speed'] == 'medium':
       x_increment = 2
else:
# This must be a fast alien.
       x_increment = 3
# The new position is the old position plus the increment. valien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#6-1 person's info in Dictionary
person_info = {'first_name': 'My',
               'last_name': 'Girl',
                'age': 25,
                'city': 'Los Angeles'}
print(person_info['first_name'])
print(person_info)

#6-2
fav_nums = {'Anthony': 7,
               'Chester': 3,
                'Dari': 25,
                'Girl1': 100,
                'Girl2': 69}
print(fav_nums['Anthony'])
print(fav_nums['Chester'])
print(fav_nums['Dari'])
print(fav_nums['Girl1'])
print(fav_nums['Girl2'])


#6-3
glossary = {'Python': 'Programming Language',
            'Visual Studio': 'Programming IDE',
            'Conditional': 'True or False test',
            'Range': 'Shows number range',
            'List': 'a list of items'}
print('Python is a \n'.title() + glossary['Python'])
print('Visual Studio is a \n'.title() + glossary['Visual Studio'])
print('A conditional is a \n'.title() + glossary['Conditional'])
print('A range \n'.title() + glossary['Range'])
print('A list is a \n'.title() + glossary['List'].title())

#KEY/NAME pairs
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
#Loop through each key/pair
glossary = {'Python': 'Programming Language',
            'Visual Studio': 'Programming IDE',
            'Conditional': 'True or False test',
            'Range': 'Shows number range',
            'List': 'a list of items'}

glossary['Loop'] = 'runs through assignment'
glossary['Nested For Loop'] = 'loop within a loop'

for definition, word in glossary.items():
    print(definition.title() + " is the definition for ".title() +
        word.title() + ".")

#6-5 Looping through dictionary keys and values
rivers = {'nile' : 'egypt',
          'great white': 'america',
          'amazon': 'brazil'}

for river, country in rivers.items():
      print("The " + river.title() + " runs through " + country.title() + ".")

for river, country in rivers.items():
      print(river.title())

for river, country in rivers.items():
      print(country.title())



favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

should_take = ['carl', 'ben', 'randy', 'jen', 'sarah', 'iver']

for name in should_take:
      if name in favorite_languages.keys():
            print(name.title() + " thank you for taking the poll")
      else:
            print(name.title() + " you need to take the poll.")

#Aliens dictionary within dictionary
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#first 3 modified
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 10 aliens.
for alien in aliens[0:10]:
    print(alien)
print("...")


#Pizza
# Store information about a pizza being ordered inside dictionary
pizza = {
       'crust': 'thick',
       #list inside a dictionary
       'toppings': ['mushrooms', 'extra cheese'],
       }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
                "with the following toppings:")
for topping in pizza['toppings']: print("\t" + topping)

#Multiple fav languages. list inside dictionary
favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
for name, languages in favorite_languages.items():
    #modified to check if there are two languages or more
    #if len(languages) >= 2:
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages: print("\t" + language.title())