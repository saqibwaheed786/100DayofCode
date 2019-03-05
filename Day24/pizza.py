#A List in a Dictionary
#Store information about a pizza being orderedself.
# -------------------------------------------------------------------------------

pizza ={
'crust':'thick',
'toppings':['mushrooms','extra chees'],
}
#Summarize the order
print("you order a "+ pizza['crust'] + "-crut pizza" + " with the following toppings:")
for topping in pizza['toppings']:
  print("\t"+ topping)
