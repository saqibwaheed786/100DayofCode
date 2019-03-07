# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
# ------------------------------------------------------------------------------

prompt = "\nWhat topping would you like on you pizza? "
prompt += "\nEnter 'quit' when you are finished "

while True:
  topping = input(prompt)
  if topping != 'quit':
    print(" I'll add " + topping + " into your pizza" )
  else:
    break
