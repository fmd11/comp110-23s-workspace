"""Ex02 one shot wordle assignment"""
__author__ = "730320788"

WORD: str = "python"
guess: str = input("What is your" + str(len(WORD)) + "-letter guess? ") 
number: int = 1
game: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes: str = ""
ind: int = 0 

while ind < len(WORD):
    if guess[ind] == WORD[ind]: 
        boxes = boxes + GREEN_BOX #if letter guess is correct add green box
    else:
        found: bool = False
        ind2: int = 0
        while ind2 < len(WORD) and not found: 
            if guess[ind] == WORD[ind2]:
                found = True
            ind2 = ind2 + 1
        if found:
            boxes = boxes + YELLOW_BOX  #if leter present in secret word add yellow box
        else:
            boxes = boxes + WHITE_BOX  #if letter is not in secret word add white box
    ind = ind + 1
print(boxes)


while game:
    if number == len(WORD):  
        print("Not quite. Play again soon!")
        exit()
    if len(guess) != len(WORD):
        input("That was not" + str(len(WORD)) + " letters! Try again:")
        number = number + 1    
    if len(guess) == len(WORD):        
        if guess == WORD: 
            print("Woo! You got it!")
            exit()
        else:
            if guess != WORD: 
                print("Not quite. Play again soon!")
                exit()

