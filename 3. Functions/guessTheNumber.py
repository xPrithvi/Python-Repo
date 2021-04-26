import random

RANDOM_NUMBER = random.randint(1, 100)

if __name__ == "__main__":
    print("Guess the number between 1 and 100, you have 10 attemps.")

    for guess_number in range(1, 11):

        valid_user_guess = False
        while valid_user_guess is False:
            try:
                user_guess = int(input(">> "))
                valid_user_guess = True
            except ValueError:
                print("Enter an integer value!")

        if user_guess > RANDOM_NUMBER:
            print("Too high! You have " + str(10 - guess_number) + " attemps remaining.")
        elif user_guess < RANDOM_NUMBER:
            print("Too low! You have " + str(10 - guess_number) + " attemps remaining.")
        else:
            break

    if user_guess == RANDOM_NUMBER:
        print("You have won! (" + str(10 - guess_number) + " attemps remaining)")
    else:
        print("Game lost!")
    input("Press any key to exit...")
