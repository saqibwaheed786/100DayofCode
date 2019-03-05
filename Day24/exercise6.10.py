# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
# -------------------------------------------------------------------------------
# for number or values we use list
favorite_numbers = {
'abbas':[20,45],
'bashir':[14,545],
'daniyal':[40,44754],
'ejaz':[55,555],
'fahad':[101,14588]
}
for name,numbers in favorite_numbers.items():
  print("This is the favorite numbers of Group Member: " + name.title() + " = " + str(numbers))
