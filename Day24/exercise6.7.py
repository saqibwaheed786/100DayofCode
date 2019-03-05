# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
# ------------------------------------------------------------------------------
people ={'saqib':{
'first':'saqib ',
'last':'waheed',
'city':'euskirche'},
'aslam':{
'first':'aslam ',
'last':'mahmood',
'city':'Koln'},
'ahmad':{
'first':'ahmad',
'last':'tanveer',
'city':'rheinbach'

},

}
for username,user_info in people.items():
    print("\nUsername:" + username)
    full_name = user_info['first']+" "+user_info['last'] # full name is equal to user info "first" and "last"
    location = user_info['city'] # location is equal to user info "city"

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title()) # location is equal to user info "city"
