"""Ex03 Wordle Assignment"""
__author__ = "730320788"

def contains_char(answer: str, letter: str) -> bool: 
    """Is letter found in word, outputs T/F"""
    assert len(letter) == 1
    ind: int = 0
    found: bool = False
    while ind < len(answer) and not found: 
        if letter[0] == answer[ind]:
            found = True
        ind = ind + 1
    if found:
        return True
    else:
        return False

def emojified(guess_word: str, answer: str) -> str:
    """creates boxes for guess / word"""
    assert len(guess_word) == len(answer)
    ind: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes: str = ""
    found: bool 
    while ind < len(guess_word):
        if guess_word[ind] == answer[ind]: 
            boxes = boxes + GREEN_BOX    
            # if letter guess is correct add green box
        else:
            found = contains_char(answer, guess_word[ind]) 
            if found == True:
                boxes = boxes + YELLOW_BOX     
                # if letter is present in the secret word, add yellow box
            if found == False:
                boxes = boxes + WHITE_BOX      
                # if letter is not in the secret word, add white box
        ind = ind + 1
    return boxes

def input_guess(length: int) -> str:
    """prompt for correct guess length"""
    guess_word: str = input("Enter a " + str(length) + " character word: ") 

    while len(guess_word) != length:
        guess_word = input(f"That wasn't " + str(length) + " chars! Try again: ")
        
    return guess_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    ind: int = 1
    answer: str = "codes"
    guess_word: str = ""
    while ind < 7 and guess_word != answer:
        print(f"=== Turn {ind}/6 ===")
        ind = ind + 1
        guess_word = input_guess(len(answer))
        print(emojified(guess_word, answer))
    if guess_word == answer: 
        print(f"You won in {ind-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")    
if __name__ == "__main__":
    main()