# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)


# alien_color = ['red',' yellow','green']
# if 'red' in alien_color:
#   print("player just earned 5 points")

# --------------------------------------------------------------------------

alien_color = ['red','yellow','green']
if 'blue' in alien_color:
  print("player just earned 5 points")
elif 'black' in alien_color:
  print("player just earned 10 points")
else:
  print("player just earned 15 points")
