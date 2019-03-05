# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
# -----------------------------------------------------------------------------------------
cities ={ 'islamabad':{
'country':'pakistan',
'population':'197 million',
'fact':'Pakistan is the worlds first Islamic country to attain nuclear power.'},
'beijing':{
'country':'china',
'population':'1.386 billion',
'fact':'In China, every year is represented by one of 12 animals.'},
'ottawa':{
'country':'canada',
'population':'36.71 million',
'fact':'Canada lowest recorded temperature was -81.4 degrees Fahrenheit (-63 C) in 1947.'
},

}
for city,country_info in cities.items():
  print("\nCountry: " + country_info['country'].title())
  country = country_info['country']
  population = country_info['population']
  fact = country_info['fact']
  print("\nCapital: " + city.title() + "," + " Country: " + country.title())
  print("Population: " + population)
  print("Facts: " +  fact)
