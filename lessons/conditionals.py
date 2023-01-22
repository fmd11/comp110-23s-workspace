"""if raining, tell me to pack umbrella"""

weather: str = input("What is the weather like?")

if (weather == "rain"):
    print("pack an umbrella!")
else:
    if (weather == "snow"):
        print("pack a jacket")
    print("You don't need an umbrella!")
print("Have a lovely day!")
