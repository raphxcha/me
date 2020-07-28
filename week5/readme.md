TODO: Reflect on what you learned this week and what is still unclear.
Refactoring: 
My countdown old format:
list = ["Getting ready to start in 3", "Getting ready to start in 2", "Getting ready to start in 1", "Let's go!"]
for element in list:
  print(element)


def countdown(message, start, stop, completion_message):
    pass
new format:
def countdown(message, start, stop, completion_message):
    while start >= stop:
        print(message + " " + str(start))
        start -= 1
    print(completion_message)

ex1 --> map() = applies a given function to each item of an iterable and returns a list as a result wordy pyramid exercise in ex1 is similar to the one we did in week4

Examples in ex2, were encouraging and gave lots of help and guidance
Koch fractals were cool too.
