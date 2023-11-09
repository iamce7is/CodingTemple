#toppings with 2 lists

current_users = ['tim', 'TOD', 'allen', 
                'bill', 'ron']
new_users = ['Sally', 'fran', 'dan',
             'tod', 'biLl']
for new_user in new_users:
    if new_user.lower() or new_user.upper() or new_user.title() in current_users:
        print("This username: " + new_user.lower() + " is in use.")
    else:
        print("This username: " + new_user.lower() + " is available.")
#print("\nFinished making your pizza!")

for i in range(len(current_users)):
    print(current_users[i])

#5-11
Nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in Nlist:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")
