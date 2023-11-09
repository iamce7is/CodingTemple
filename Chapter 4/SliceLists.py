cars = ['Lamborghini', 'Porsche', 'Ferarri', 'Rolls Royce', 'Mclaren', 'Aston Martin']
print("The first three items on my list are: ")
for car in cars[:3]:
    print(car)

print("The Middle three items on my list are: ")
for car in cars[2:5]:
    print(car)

print("The last three items on my list are: ")
for car in cars[-3:]:
    print(car)

Pizzas = ['Hawaiian', "Supreme", 'Margharita']
friend_pizzas = Pizzas[:]
print(friend_pizzas)

Pizzas.append("Diavola")
friend_pizzas.append('4 Cheese')
print(Pizzas)
print(friend_pizzas)

#4-11/4-12
print("My favorite Pizzas are: ")
for pizza in Pizzas:
    print(pizza)

print("My friends favorite Pizzas are:")
for Fpizza in friend_pizzas:
    print(Fpizza)

#4-13
menu = ("Chicken", "Pizza", "Sushi", "Burger", "Pie")
for i in menu:
    print(i)

#menu.append("Pork")
#print(menu)

menu = ("Chicken", "Pizza", "Sushi", "Pasta", "Pork")
for i in menu:
    print(i)