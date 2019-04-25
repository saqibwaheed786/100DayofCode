# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
# _________________________________________________________________________________
def describe_city(city, country='pakistan'):
  """Describe city."""
  msg= city.title() + " is in " + country.title() + "."
  print(msg)

describe_city("lahore")
describe_city("karachi")
describe_city('dhali ', 'india')
