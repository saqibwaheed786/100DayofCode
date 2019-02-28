# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
# --------------------------------------------------------------------------------------
favorite_numbers = {
'abbas':20,
'bashir':14,
'daniyal':40,
'ejaz':55,
'fahad':101}
for name,numbers in favorite_numbers.items():
  print("This is the favorite number of Group Member: " + name.title() + " = " + str(numbers))
