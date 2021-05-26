NAMES = []

while True:
    print("Enter username No." + str(len(NAMES) + 1))
    user_name = input(">> ")
    if user_name != "":
        NAMES.append(user_name)
    else:
        break
print(NAMES)
