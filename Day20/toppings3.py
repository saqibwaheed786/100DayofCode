# requested_toppings =['mushroom','green pappers','extra cheese']
# for requested_topping in requested_toppings:
#   print("Adding " + requested_topping + "." )
# print("\nFinishe making you pizza!")

# But what if the pizzeria runs out of green peppers? An if statement
# inside the for loop can handle this situation appropriately:

# requested_toppings =['mushroom','green pappers','extra cheese']
# for requested_topping in requested_toppings:
#   if requested_topping == 'green pappers':
#     print("Sorry, we are out of green pappers right now")
#   else:
#     print("Adding " + requested_topping + "." )
# print("\nFinishe making you pizza!")

# -----------------------------------------------------------------------------
# Checking That a List Is Not Empty
# requested_toppings =[]
# if requested_toppings:
#   for requested_topping in requested_toppings:
#     print("Adding " + requested_topping + ".")
#   print("\nFinishe making you pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
# -----------------------------------------------------------------------------

# Using Multiple Lists
available_toppings = ['mushroom','oliven','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print("Adding " + requested_topping + ".")
  else:
    print("Sorry we don't have " + requested_topping + "." )
print("\nFinishe making your Pizza!")
