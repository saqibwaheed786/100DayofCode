# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

hello_admin =[]
if hello_admin:
	for username in hello_admin:
		print("we need to find some users!" + username+ ".")
	else:
		print("\nwe need to find some users!")
