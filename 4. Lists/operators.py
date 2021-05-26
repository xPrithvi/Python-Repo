NAMES = ["Bill", "Richie", "Ben", "Eddie", "Mike", "Beverly"]

while True:
    searched_name = input("Give a member of The Losers' Club: ")

    if searched_name is "":
        break
    elif (searched_name in NAMES) is True:
        print("Correct!")
    else:
        print("Wrong!")
