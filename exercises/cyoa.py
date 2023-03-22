"""Choose Your Own Adventure Experience - EX06."""

__author__ = "730320788"

from random import randint

points: int = 0
# tracks adventure points. 
player: str 
# player's name.
kisses: str = "\U0001F617"
# kiss emoji.


def main() -> None:
    """The main game function."""
    global points 
    global player
    greet()
    begin: str = input("Type 'go' to begin the game or type 'stop' to end the game. Or if you're sad type 'cheer me up' to get a little kiss, lol. ")
    if begin != "stop":
        if begin != "go":
            if begin != "cheer me up":
                print("sorry that wasn't an option.")
    if begin == "stop":
        print(f"Thanks for stopping by {player}. You earned {points} points while you were playing. See you again soon!")
    while begin == "cheer me up":
        kiss()
        begin = "go"
    while begin == "go":
        if begin == "go":
            go()  
            points += go()
        begin = input(f"You have {points} points right now! Would you like to keep playing? stop or go? ")
             

def greet() -> None:   
    """Greets the player and introduces the game."""
    name: str = input("Hello player! What's your name?  ")
    global player 
    player = name 
    print(f"Welcome to the Coin toss game {player}!  In this game you can make a guess if our coin will land on heads or tails. Then we will flip the coin and you win points if you guessed correctly!")


def kiss() -> None:
    """Gives bonus point to sad player."""
    global points
    global player
    global kisses 
    print(f"oh no! Don't be sad {player}. {kisses}")
    bonus: str = input("Are you feeling beter yet or do you need a bonus point? yes or no? ")
    if bonus == "yes":
        print(f"ok just one more point to cheer you up! now you have {points + 1}!")
        points = points + 1 
    if bonus == "no":
        print("ok glad you are feeling better!")


def go() -> int:
    """Player makes a guess and flips the coin."""
    global player
    global points
    game: bool = True
    guess: str = input("Go ahead and guess 'heads' or 'tails'! ")  
    if guess == "heads": 
        print(f"Ok, {player} you chose heads! You must like looking at a pretty face \U0001F609")
        while game:
            flip: str = input("Now to flip the coin type flip. ")
            if flip == "flip":
                x: int = randint(0, 1)
                game = False 
            else:
                print("sorry this game can only go on if you flip the coin")
        if x == 0: 
            print(f"yay! It was heads! You gained a point! now you have {points + 1}")
            return 1
        if x == 1: 
            print(f"oh no! It was tails. No more points this time. You still have {points}")
            return 0
    if guess == "tails":
        print(f"Ok, {player} you chose tails!")
        while game:
            flip = input("Now to flip the coin type flip. ")
            if flip == "flip":
                x = randint(0, 1)
                game = False 
            else:
                print("sorry this game can only go on if you flip the coin")
        if x == 1: 
            print(f"yay! It was tails! You gained a point! now you have {points + 1}")
            return 1
            # player guessed correctly.
        if x == 0: 
            print(f"oh no! It was heads. No more points this time. You still have {points}")
            return 0
    else: 
        return 0