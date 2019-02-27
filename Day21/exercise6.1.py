# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
# --------------------------------------------------------------------------------------
user ={'saqib':{'first':'saqib ',
'last':'waheed',
'city':'euskirche'},
'aslam':{'first':'aslam ',
'last':'mahmood',
'city':'Koln'}
}
for username,user_info in user.items():
    print("\nUsername:" + username)
    full_name = user_info['first']+""+user_info['last'] # full name is equal to user info "first" and "last"
    location = user_info['city'] # location is equal to user info "city"

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title()) # location is equal to user info "city"
