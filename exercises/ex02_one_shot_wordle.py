"""Ex02 one shot wordle assignment."""

__author__ = "730320788"

WORD: str = "python"
guess: str = input("What is your " + str(len(WORD)) + "-letter guess? ") 
game: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes: str = ""
ind: int = 0 

while game:
    if len(guess) != len(WORD):
        guess = input(f"That was not {len(WORD)} letters! Try again:")
    else:
        while ind < len(WORD):
            if guess[ind] == WORD[ind]: 
                boxes = boxes + GREEN_BOX    
                # if letter guess is correct add green box
            else:
                ind2: int = 0
                found: bool = False
                while ind2 < len(WORD) and not found: 
                    if guess[ind] == WORD[ind2]:
                        found = True
                    ind2 = ind2 + 1
                if found:
                    boxes = boxes + YELLOW_BOX     
                    # if letter is present in the secret word, add yellow box
                else:
                    boxes = boxes + WHITE_BOX      
                    # if letter is not in the secret word, add white box
            ind = ind + 1
        print(boxes)
        if guess == WORD:
            print("Woo! You got it!")
            game = False
            # response to correct guess 
        else:
            print("Not quite. Play again soon!")
            game = False