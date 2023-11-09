input2 = input("What kind of car would you like to rent? ")
print("I will get you the baddest " + input2 + "!")

input1 = input("How many people are coming to dinner?")
input1 = int(input1)
if input1 >= 8:
    print("You will have to wait for a table.")
else:
    print("You will all be seated by the windows.")

number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")

#While
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
       message = input(prompt)

       if message != 'quit':
           print(message)

#Flag to set active/inactive state
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True 
while active:
       message = input(prompt)
if message == 'quit': 
     active = False
else: print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
           break
    else:
           print("I'd love to go to " + city.title() + "!")
