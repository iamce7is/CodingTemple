#8-1
def ch8():
    """Display what we are learning."""
print("In Chapter 8, we are learning about functions in Python")
ch8()



#8-2
book = ''
def favourite_book(book):
    """Display what we are learning."""
    print("My current favourite book is: " + book)
favourite_book('I forgot to die')

#Pets function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#8-3 positional
def make_shirt(shirt_size, shirt_text):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text)

make_shirt('Small', 'Howdy there!')


#positional/predefined
def make_shirt(shirt_size, shirt_text='Howdyyy'):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text)

make_shirt('Small')

#keyword arguments
def make_shirt(shirt_size, shirt_text):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text.title())

make_shirt(shirt_size='XL', shirt_text='To infinity and beyond!')

#8-4
def make_shirt(shirt_size='Large', shirt_text='I Love Python'):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text)

make_shirt()

def make_shirt(shirt_size='Medium', shirt_text='I Love Python'):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text)

make_shirt()

def make_shirt(shirt_size='XS', shirt_text='I Love P*******s'):
    """message about size and text"""
    print("The shirt size is " + shirt_size + " and the message reads: " + shirt_text)

make_shirt()

#8-5
def describe_city(city, country='USA'):
    """City/Country message"""
    print('The City of ' + city + ' is in ' + country)

describe_city('Los Angeles')

def describe_city(city, country='USA'):
    """City/Country message"""
    print('The City of ' + city + ' is in ' + country)

describe_city('New York')

def describe_city(city, country='USA'):
    """City/Country message"""
    print('The City of ' + city + ' is in ' + country)

describe_city('Monterrey N.L.', 'Mexico')


def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full name, neatly formatted."""
    if middle_name:
     full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
           break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#Put attention
def city_name(city_n, city_c):
    """format"""
    formattedcity_ =  city_n + ', ' + city_c
    return formattedcity_.title()
#
#named_city = input('What is the name of the city?')
#named_country = input('What country is the city in? ')

#city_namefunc = city_name(named_city, named_country
#print(city_namefunc)

city1 = city_name('Paris', 'France')
city2 = city_name('Los Angeles', 'USA')
city3 = city_name('Havana', 'Cuba')

print(city1)
print(city2)
print(city3)

"""def make_album(artist_name, album_title, tracks=''):"""
    """album info"""
   """ album_dict = {artist_name: album_title}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

   # albumdict1 = {artist_name: album_title}
   # albumdict2 = {artist_name: album_title}
    
   #albums = [album_dict, albumdict1, albumdict2]

dict1a = input('What is the artist\'s name? ')
dict1b = input('What is the album title? ')
dict1c = input('How many tracks are on the disk? ')

dict2a = input('What is the artist\'s name? ')
dict2b = input('What is the album title? ')
dict2c = input('How many tracks are on the disk? ')


dict3a = input('What is the artist\'s name? ')
dict3b = input('What is the album title? ')

dictionary_info = make_album(dict1a, dict1b, dict1c)

print(dictionary_info)

dictionary_info = make_album(dict2a, dict2b, dict2c)

print(dictionary_info)

dictionary_info = make_album(dict3a, dict3b)

print(dictionary_info)"""



def make_album(artist_name, album_title, tracks=''):
    """album info"""
    album_dict = {artist_name: album_title}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

   # albumdict1 = {artist_name: album_title}
   # albumdict2 = {artist_name: album_title}
    
   #albums = [album_dict, albumdict1, albumdict2]

while True:
    print("Give us the Artist info: \n")
    print("(Enter q anytime to quit \n)")

    dict1a = input('What is the artist\'s name? ')
    dict1b = input('What is the album title? ')
    dict1c = input('How many tracks are on the disk? ')
    if dict1a or dict1b or dict1c == 'q':
        break

    dict2a = input('What is the artist\'s name? ')
    dict2b = input('What is the album title? ')
    dict2c = input('How many tracks are on the disk? ')
    if dict2a or dict2b or dict2c == 'q':
        break

    dict3a = input('What is the artist\'s name? ')
    dict3b = input('What is the album title? ')
    if dict3a or dict3b == 'q':
        break

dictionary_info = make_album(dict1a, dict1b, dict1c)

print(dictionary_info)

dictionary_info = make_album(dict2a, dict2b, dict2c)

print(dictionary_info)

dictionary_info = make_album(dict3a, dict3b)

print(dictionary_info)