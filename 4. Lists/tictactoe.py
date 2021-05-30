BOARD = ["EMPTY", "EMPTY", "EMPTY",
         "EMPTY", "EMPTY", "EMPTY",
         "EMPTY", "EMPTY", "EMPTY"]

while True:
    print("Cross' Turn. Which cell?")
    cell_number = int(input(">> "))
    BOARD[cell_number - 1] = "X"
    print("")
    print(BOARD)

    print("Noughts' Turn. Which cell?")
    cell_number = int(input(">> "))
    BOARD[cell_number - 1] = "O"
    print("")
    print(BOARD)
