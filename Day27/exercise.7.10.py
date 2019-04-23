# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one p
# lace in the world, where would you go? Include a block of code
# that prints the results of the poll.

name_prompt = "\nWhat's your name?"
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWourld you like to go with someone else ;-)? (yes/no) "

#Responses will be stored in the form { name: place}
responses = {}
while True:
  #Ask the user where they'd like to go.
  name = input(name_prompt)
  place =input(place_prompt)

  #store the  response.
  responses[name] = place
  #Ask if there's anyone else responding.
  repeat = input(continue_prompt)
  if repeat != 'yes':
    break
    #show result of the survey.
print("\n---- Result ----")
for name, place in responses.items():
  print(name.title() + " Would like to visit " + place.title() + "." )
