"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will print each word from the list above by calling the print function.
for word in some_words:
    print(word) #it printed the list of words each time you execute print

# I think this will print each word from the list above by calling the print function.
for x in some_words:
    print(x) # did the exact same thing as line 17 and 18

# I think this will print the list
print(some_words)

# I think this will print no. 4, 5 and 6 by calling the print function.
if len(some_words) > 3: # It printed 6 because this is larger than 3.
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
