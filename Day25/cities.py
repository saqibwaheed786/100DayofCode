prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"
while True: #A loop that starts with while True u will run forever unless it reaches a
# break statement.
  city = input(prompt)
  if city == 'quit':
    break
  else:
    print("I'd love to go to " + city.title() +"!" )
