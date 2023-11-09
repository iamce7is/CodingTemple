prompt = "\nTell me the kind of pizza you want..."
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    while message != 'quit':
       message = input(prompt)

       if message != 'quit':
           print("We will make you a pizza with the following topppings: " + message)
    else:
         active = False

prompt = "\nTell me the kind of pizza you want now..."
prompt += "\nEnter 'quit' to end the program. "
message = ""

#active = True
#while active:
active = True
while active: 
    while message != 'quit':
          message = input(prompt)
          if message != 'quit':
             print("We will make you a pizza with the following topppings: " + message)
          elif message == 'quit':
           active = False
