# 8.4 Large T-Shirt: Modify the make_shirt() function so that shirts are large by default with a message 
# that reads I love Python. Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message
def make_shirt(size="Large", message="I Love Python"):
    """Summarize the shirt that's going to be made."""
    print("\nI am going to make a " + size + " T-shirt ")
    print("It will say," + message)

make_shirt() #Position arguments
make_shirt(size="Medium")#one Keyword arguments
make_shirt("Small", "Programmers are loopy.")