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
    print("Give us the Artist info: ")
    print("(Enter q anytime to quit) \n")

    dict1a = input('What is the artist\'s name? ')
    if dict1a == 'q':
        break
    dict1b = input('What is the album title? ')
    if dict1b == 'q':
        break
    dict1c = input('How many tracks are on the disk? ')
    if dict1c == 'q':
        break
    
   
    dict2a = input('What is the artist\'s name? ')
    if dict2a == 'q':
        break
    dict2b = input('What is the album title? ')
    if dict2b == 'q':
        break
    dict2c = input('How many tracks are on the disk? ')
    if dict2b == 'q':
        break

    dict3a = input('What is the artist\'s name? ')
    if dict3a == 'q':
        break
    dict3b = input('What is the album title? ')
    if dict3b == 'q':
        break

    dictionary_info = make_album(dict1a, dict1b, dict1c)

    print(dictionary_info)

    dictionary_info = make_album(dict2a, dict2b, dict2c)

    print(dictionary_info)

    dictionary_info = make_album(dict3a, dict3b)

    print(dictionary_info)

def greet_users(names):
       """Print a simple greeting to each user in the list."""
       for name in names:
           msg = "Hello, " + name.title() + "!"
           print(msg)
usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)

def print_models(unprinted_designs, completed_models): 
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed.""" 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
           print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


