def get_formatted_name(first_name, last_name):
  """Return a full name, neastly formatted."""
  full_name = first_name + '' + last_name
  return full_name.title()

musician = get_formatted_name('saqib ', 'malik ')
print(musician)   
