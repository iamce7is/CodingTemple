prompt = "\nTell me the kind of pizza you want..."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
       message = input(prompt)

       if message != 'quit':
           print("We will make you a pizza with the following topppings: " + message)

#with break
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break


prompt1 = input("What is your age? ")
while True:
    age = input(prompt1)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your admission is free.")
    elif age < 13:
        print("Your admission is $10.")
    else:
        print("Your admission is $15.")

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
