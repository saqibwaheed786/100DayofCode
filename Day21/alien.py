# alien_0 ={'color':'green','points':5 }
# print(alien_0['color'])
# print(alien_0['points'])

# ---------------------------------------------------------------------------
                                #Points
# alien_0 ={'color':'green','points':5 }
# new_points = alien_0['points']
# print("You just got " +str(new_points)+ " points!")
# ---------------------------------------------------------------------------

                                 #Position
# alien_0 ={'color':'green','points':5 }
# print(alien_0)
#
# alien_0['x_position'] =0
# alien_0['y_position']=25
# print(alien_0)
# ---------------------------------------------------------------------------

                    #starting with an Empty Dictionary

# alien_0 ={}
#
# alien_0['color']= 'green'
# alien_0['points'] =5
# print(alien_0)

# ---------------------------------------------------------------------------
#                    # Modifying Values in a Dictionary
# alien_0 ={'color':'green'}
# print("The alien is " + alien_0['color'] + "." )
#
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ". " )
# ---------------------------------------------------------------------------
              # Alien Speed calculation

# alien_0 ={'x_position':0, 'y_position':25, 'speed':'slow'}
# print("Original X-Position "+ str(alien_0['x_position']))
# # Move the alien to the right
# # Determine how far to move the alien based on its current speed.
#
# if alien_0['speed']== 'slow':
#   x_increment =1
# elif alien_0['speed'] == 'medium':
#   x_increment =2
# else:
#    # This must be a fast alien
#   x_increment =3
# # The nw position is the old position plus the increment
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-Positon:" + str(alien_0['x_position']))
# ---------------------------------------------------------------------------
                               #Removing Key-Value Pairs
alien_0 ={'color':'green','position':5 }
print(alien_0)

del alien_0['position']
print(alien_0)
