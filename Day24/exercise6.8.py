# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
# ---------------------------------------------------------------------------------
pets = { 'dog':{
'owner_name':'malik',
'breeds':'german shephred',
'colors':'black and brown',
'qualitie':'They can read our emotions.'},
'cat':{
'owner_name':'aisha',
'breeds':'persian cat',
'colors':'white',
'qualitie':'friendly, active, loving, independent.'},
'rabbit':{
'owner_name':'rabia',
'breeds':'florida white',
'colors':'white',
'qualitie':'polite, sensitive, furry'},

}

for pet_type,pet_info in pets.items():
  print("\nPet Type: "+ pet_type)
  owner = pet_info['owner_name']
  breed = pet_info['breeds']
  color = pet_info['colors']
  qualities =pet_info['qualitie']

  print("\nOwner: " + owner.title())
  print("Breed: "+ breed.title())
  print("Color: " + color.title())
  print("Qualities: " + qualities.title())
