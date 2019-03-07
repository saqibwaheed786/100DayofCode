                   # Letting the User Choose When to Quit
# prompt = "\nTell me something and i will repeat it back to you:"
# prompt += "\nOr enter 'quit' to end program. "
# message =""
# while message !='quit':
#   message = input(prompt)
#   print(message)


# ------------------------------------------------------------------------------
                                  # Using a Flag
prompt = "\nTell me something and i will repeat it back to you:"
prompt += "\nOr enter 'quit' to end program. "
active = True  # programe start in an active state
while active:
  message = input(prompt)
  
  if message == 'quit': #if user enters 'quit' we set active to False 
    active =False
  else:  # if user enter anything other then 'quit' we print their input as a message 
    print(message)
