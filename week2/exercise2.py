"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
Remeber that all files must also pass the
linter with no errors or warnings!
"""

import string

def GetLetter(index):
    alphabet = string.ascii_lowercase + " "
    return alphabet

def week2exersise2():
    indices = [12, 2, 26, 7, 0, 12, 4, 17]
    WordArray[] = map(GetLetter, indices)
    (WordArray[0] = WordArray[0].upper())
    (WordArray[1] = WordArray[1].upper())
    (WordArray[3] = WordArray[3].upper())
    secret_word ="".join(WordArray)
    print(secret_word)
    return secret_word


if __name__ == "__main__":
    print(week2exersise2())