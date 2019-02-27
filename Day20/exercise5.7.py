# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favorite_fruits = ['banana','apple','kiwi','mango','pineapple']
if 'banana' in favorite_fruits:
  print("i like to eat banana")
  if 'apple' in favorite_fruits:
    print("i like to eat apple")
  if 'kiwi' in favorite_fruits:
      print("i like to eat kiwi")
      if 'mango' in favorite_fruits:
        print("i like to eat mango")
        if 'pineapple' in favorite_fruits:
          print("i like to eat pineapple")
