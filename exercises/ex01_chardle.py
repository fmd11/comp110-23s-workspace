"""Chardle - Comp 110 EX01""" 

__author__ = "730320788"

word: str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if  len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(letter) < 1:
    print("Error: Character must be a single character.")
    exit()

number: int = 0

print("Searching for " + letter + " in "+ word)

if letter == word[0]:
    print(letter + " found at index 0")
    number += 1
if letter == word[1]:
    print(letter + " found at index 1")
    number += 1
if letter == word[2]:
    print(letter + " found at index 2")
    number += 1
if letter == word[3]:
    print(letter + " found at index 3")
    number += 1
if letter == word[4]:
    print(letter + " found at index 4")
    number += 1

if number == 0:
    print("No instances of " + letter + " found in " + word)
if number == 1:
    print("1 instance of " + letter + " found in " + word)
if number == 2:
    print("2 instance of " + letter + " found in " + word)
if number == 3:
    print("3 instance of " + letter + " found in " + word)
if number == 4:
    print("4 instance of " + letter + " found in " + word)
if number == 5:
    print("5 instance of " + letter + " found in " + word)





