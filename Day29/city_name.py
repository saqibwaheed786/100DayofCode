# #8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country . 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value . 
# Call your function for three different cities, 
# at least one of which is not in the default country .
def city_country(city, country):
    """Return a string like 'Lahore, Pakistan.'."""
    return(city.title()) + " " + country.title()


city = city_country('lahore', 'pakistan')
print(city)

city = city_country('karach', 'pakistan')
print(city)

city = city_country('agra', 'india')
print(city)
