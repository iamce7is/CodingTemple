x= 1
while x <= 5:
    print(x)
    x += 1

#7-8
sandwich_orders = ['tuna', 'garlic', 'steak', 'cheese']
finished_sandwiches = []

for sw in sandwich_orders:
    if sw not in finished_sandwiches:
        print("Your " + sw + " sandwich is ready!")
        finished_sandwiches.append(sw)
print(finished_sandwiches)



sandwich_orders = ['pastrami', 'tuna', 'garlic', 'pastrami', 'steak', 'cheese', 'pastrami']
print('Sorry, we are all out of pastrami...')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)



sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")



responses = {}
   # Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
       # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to go someday? ")
       # Store the response in the dictionary.
    responses[name] = response
       # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
           polling_active = False
   # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
       print(name + " would like to go visit " + response + ".")