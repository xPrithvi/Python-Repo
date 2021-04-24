def collatz(number):

    # Even number.
    if number %2 == 0:
        number = number // 2

    # Odd number.
    elif number %2 == 1:
        number = 3*number + 1

    return number

if __name__ == "__main__":
    number = int(input("Enter number: "))
    while number != 1:
        print(number)
        number = collatz(number)
    print("1")
    input("Press any key to exit...")

        
        
