names = ['Tom', 'Travis', 'Mark', 'Elias', 'Jim']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

message = "Hello to the one named " + names[0].title() + "."
print(message)

message = "Hello to the one named " + names[1].title() + "."
print(message)

message = "Hello to the one named " + names[2].title() + "."
print(message)

message = "Hello to the one named " + names[3].title() + "."
print(message)

message = "Hello to the one named " + names[4].title() + "."
print(message)


cars = ['Lamborghini', 'Porsche', 'Ferarri', 'Rolls Royce']
message = "I will own a " + cars[0].title() + " one day real soon."
print(message)

message = "I will own a " + cars[1].title() + " one day real soon."
print(message)

message = "I will own a " + cars[2].title() + " one day real soon."
print(message)

message = "I will own a " + cars[3].upper() + " one day real soon."
print(message)

cars[3] = ('Bugatti')
message = "I will own a " + cars[3].upper() + " one day real soon."
print(message)

print(cars)

cars.append('Rolls Royce')
print(cars)

cars.insert(0, 'Mclaren')
print(cars)

del cars[2]
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)

first_get = cars.pop(1)
print(first_get)

message = "I will first get a " + first_get
print(message)

print(cars)

cars.remove('Ferarri')
print(cars)
