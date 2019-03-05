# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
# ----------------------------------------------------------------------------------
favorite_places = {'armeena':{
'fav_ple': 'lahore, karachi'
},
'beenish':{
'fav_ple':'gilgit, islamabad'
},
'gubadin':{
'fav_ple':'neelum valley, shangrila resort :-)'
}
}
for name,place in favorite_places.items():
  if name in favorite_places:
    print("\n")
    print(name.title() + ":" + " Waht is your favorite place?")
    favorite = place['fav_ple']
    print(name.title()+ ": "+ favorite.title())
