# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
# ----------------------------------------------------------------------------
favorite_languages ={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python'
}
for name,language in favorite_languages.items():
  print(name.title() + "'s favorite language is " + language +"." )

print("\n")

coders = {'phil',
  'josh', 'david', 'becca',
  'sarah', 'matt', 'danielle'
  }
for coder in coders:
    if coder in favorite_languages.keys():
      print("Thank you for taking the pool," + coder.title() )
    else:
      print(coder.title()+ ", Waht is your favorite language?")
