
age = 12
if age < 4:
    price = 0 
elif age < 18:
    price = 5 
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#Aliens
alien_colour = 'Green'
if alien_colour == 'Green':
    print('You have earned 5 points!')

alien_colour = 'Red'
if alien_colour == 'Green':
    print('You have earned 5 points!')

#5-4
alien_colour = 'Green'
if alien_colour == 'Green':
    print('You have earned 5 points!')
else:
    print('You have earned 10 points!')

alien_colour = 'Red'
if alien_colour == 'Green':
    print('You have earned 5 points!')
else:
    print('You have earned 10 points!')

#5-5
alien_colour = 'Green'
if alien_colour == 'Green':
    print('You have earned 5 points!')
elif alien_colour == 'Yellow':
    print('You have earned 10 points!')
else:
    print("You have earned 15 points!")

alien_colour = 'Yellow'
if alien_colour == 'Green':
    print('You have earned 5 points!')
elif alien_colour == 'Yellow':
    print('You have earned 10 points!')
else:
    print("You have earned 15 points!")

alien_colour = 'Red'
if alien_colour == 'Green':
    print('You have earned 5 points!')
elif alien_colour == 'Yellow':
    print('You have earned 10 points!')
else:
    print("You have earned 15 points!")

#5-6
age = 70
if age == 2:
    print('This is a baby')
elif age >= 2 and age <= 4:
    print('Toddler')
elif age >= 4 and age <= 13:
    print('Kid')
elif age >= 13 and age <= 20:
    print('Teenager')
elif age >= 20 and age <= 65:
    print('Adult')
else:
    print('Elder')

#5-7
Fruits = ['Apple', 'Pineapple', 'Kiwi', 'Pear', 'Grapes']
if 'Apple' in Fruits:
    print('You love Apples')
if 'Pineapple' in Fruits:
    print('You love Pineapple')
if 'Kiwi' in Fruits:
    print('You love Kiwi')
if 'Pear' in Fruits:
    print('You love Pear')
if 'Grapes' in Fruits:
    print('You love Grapes')

#toppings with 2 lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

#5-8
"""Usernamess = ['Tod', 'Eva', 'Admi', 'Bon', 'Raul']
for Username in Usernamess:
    if Username == 'Admin':
        print("Hello Admin")
    else:   
        print("Hello " + Username)
"""

user = input('Enter Username: ').lower()

user_names = ["eric", "admin", "lever", "matt"]

if user in user_names:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else: 
        print(f'Hello {user.title()}, thank you for logging in again.')

else:
    print('Not in list')



user = input('Enter Username: ').lower()

user_names = []

if user in user_names:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else: 
        print(f'Hello {user.title()}, thank you for logging in again.')

else:
    print('We need users')


#toppings with 2 lists

current_users = ['tim', 'tod', 'allen', 
                'bill', 'ron']
new_users = ['sally', 'fran', 'dan',
             'tod', 'bill']
for new_user in new_users:
    if new_user in current_users:
        print("Hello " + new_user + ".")
    else:
        print("Sorry, we don't have " + new_user + " your account.")
#print("\nFinished making your pizza!")