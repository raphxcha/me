"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("\nI'm thinking of a number between 1 and 100.")
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)
    actualnumber = random.randint(lowerBound, upperBound)
    guessed = False
    x = False
    z = ValueError

    while x == False:
        y = False
        while y != True:
            lowerBound = input("Guess a smaller number: ")
            try:
                int(lowerBound)
                y = True
            except z:
                print("Invalid Response - Integer Only, try again: ")
                y = False
            y1 = False
            while y1 != True:
                upperBound = input("Guess a higher number: ")
                if upperBound > lowerBound:
                    try:
                        int(upperBound)
                        x = True
                        y1 = True
                    except z:
                        print("Invalid Response - Integer Only, try again: ")
                        upperBound = input("Guess a higher number: ")
                        y1 = False
                    else:
                        print("Guess lower, not higher!")
                        y1 = False
                print("Guess a number between" + str(lowerBound) + "and" + str(upperBound))

        

        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == realnum:
            print("You got it!! It was {}".format(realnum))
            guessed = True
        elif guessedNumber < realnum:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
        if wronginput:
            print("This response is invalid, try again: ")
    
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
