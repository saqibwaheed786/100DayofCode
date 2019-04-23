# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a quit value.
# ----------------------------------------------------------------------------------------

prompt = "\nWhat topping would you like on you pizza? "
prompt += "\nEnter 'quit' when you are finished "
active = True
while active:
  topping = input(prompt)

  if topping == 'quit':
    active = False
  else:
    print(" I'll add " + topping + " into your pizza" )
