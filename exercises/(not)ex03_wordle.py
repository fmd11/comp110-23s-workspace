"""Ex03 Wordle Assignment"""
__author__ = "730320788"

def contains_char(answer: str, letter: str) -> bool: 
    """Is letter found in word, outputs T/F"""
    assert len(letter) == 1
    found: bool = False
    turn: int = 0
    while turn < len(answer) and not found: 
        if letter[0] == answer[turn]:
            found = True
        turn = turn + 1
    if found:
        return True
        #letter was found
    else:
        return False
        #letter not found

def input_guess(length: int) -> str:
    """prompt for correct guess length"""
    guess_word: str = input("Enter a " + str(length) + " character word: ") 

    while len(guess_word) != length:
        guess_word = input(f"That wasn't " + str(length) + " chars! Try again: ")
        
    return guess_word

def emojified(guess_word: str, answer: str) -> str:
    """creates boxes for guess / word"""
    assert len(guess_word) == len(answer)
    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes: str = ""
    turn: int = 0
    found: bool 
    while turn < len(guess_word):
        if guess_word[turn] == answer[turn]: 
            boxes = boxes + GREEN_BOX    
        else:
            found = contains_char(answer, guess_word[turn]) 
            if found == False:
                boxes = boxes + WHITE_BOX      
            if found == True:
                boxes = boxes + YELLOW_BOX     
        turn = turn + 1
    return boxes


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    answer: str = "codes"
    guess_word: str = ""
    while guess_word != answer and turn < 6:
        print(f"=== Turn {turn+1}/6 ===")
        turn = turn + 1
        guess_word = input_guess(len(answer))
        print(emojified(guess_word, answer))
    if guess_word == answer: 
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")    
if __name__ == "__main__":
    main()