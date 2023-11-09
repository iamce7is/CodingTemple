def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

def make_sw(*toppings):
    """Summarize the sw we are about to make."""
    print("\nMaking a sw with the following ingredients:")
    for topping in toppings:
        print("- " + topping)

make_sw('ham')
make_sw('mushrooms', 'green peppers', 'extra cheese')

make_sw('Turkey')
make_sw('lurkey', 'jerky', 'furkey')

make_sw('Tuna')
make_sw('lettuce', 'cheese', 'peppers')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('anthony', 'celis',
                             location='los angeles',
                             field='software',
                             music='hip-hop')
print(user_profile)


def buildcar_profile(car_make, car_model, **car_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['car'] = car_make
    profile['model'] = car_model
    for key, value in car_info.items():
        profile[key] = value
    return profile
car_profile = buildcar_profile('lamborghini', 'aventador',
                             location='los angeles',
                             color='black',
                             year='2024')
print(car_profile)