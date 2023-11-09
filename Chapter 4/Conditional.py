#equality of strings
name1 = "John"
name2 = "Jon"
name3 = "John"

if (name1 == name3):
    print("Equal")
else:
    print("Unequal")

#inequality of strings

if(name1 != name2):
    print("Unequal")
else:
    print("Equal")

#Numerical
age1 = 18
age2 = 23

if(age1 == 18):
    print("Eligable to vote")

if(age1 != 23):
    print("Cannot drink")

if(age1 <= age2):
    print("Younger")

if(age2 >= age1):
    print("Older")

# and/or keyword
if (age1 == 18 or age2==23):
    print("Can vote")

if(age1 == 18 and age2 == 23):
    print("both are adults")

car = 'Audi'
if(car.lower() == 'audi'):
    print('True')

car = 'Audi'
if car == 'audi':
    print('True')
else:
    print("False")


## Item in list or not
fruits = ['apple','peach','melon']
if 'apple' in fruits:
    print("Apple is present in fruits")
if 'guava' not in fruits:
    print("Guava is not present in fruits")