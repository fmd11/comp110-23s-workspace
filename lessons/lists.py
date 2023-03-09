"""Practice with lists."""
grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"

grocery_list.pop(2)


names: list[str] = ["a", "b", "c"]
for idx in range(0,3):
    print(names[idx])
