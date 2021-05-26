# Creating a list.
LIST = ["Cat", "Bat", "Rat", "Elephant"]
print("Created a list: " + str(LIST))

# Printing the individual items of the list.
print(">> Printing the individual items of the list.")
print(LIST[0])
print(LIST[1])
print(LIST[2])
print(LIST[3])
print("")

# Printing the individual items of the list using negative indexes.
print(">> Printing the individual items of the list (using negative indexes).")
print(LIST[-4])
print(LIST[-3])
print(LIST[-2])
print(LIST[-1])
print("")

# Printing sections of the list using slices.
print(">> Printing specific sections of the list using slices.")
print(LIST[1:3])
print(LIST[0:2])
print(LIST[0:-1])
print("")

# Printing the length of the list.
print(">> Printing the length of the list.")
print("There are " + str(len(LIST)) + " items in the list.")
print("")

# Changing items in the list.
print(">> Changing items in the list.")
print("Before: " + str(LIST))
LIST[0] = "Tiger"
LIST[3] = "Lion"
LIST[2] = LIST[1]
print("After: " + str(LIST))
print("")

# Creating a list within a list.
NESTED_LIST = [LIST, [10, 20, 30, 40, 50]]
print("Created a nested list: " + str(NESTED_LIST))

# Printing the items of the nested list.
print(">> Printing the items of the nested list.")
print(NESTED_LIST[0])
print(NESTED_LIST[1])
print("")

# Printing all items contained within the nested list.
print(">> Printing all items contained within the nested list.")
print(NESTED_LIST[0][0])
print(NESTED_LIST[0][1])
print(NESTED_LIST[0][2])
print(NESTED_LIST[0][3])

print(NESTED_LIST[1][0])
print(NESTED_LIST[1][1])
print(NESTED_LIST[1][2])
print(NESTED_LIST[1][3])
print(NESTED_LIST[1][4])
print("")

# Creating new lists.
LIST_2 = [1, 2, 3]
print("Created a list: " + str(LIST_2))

LIST_3 = ["A", "B", "C"]
print("Created a list: " + str(LIST_3))

# Combining the lists.
print(">> Combining the above lists.")
COMBINED_LIST = LIST_2 + LIST_3
print(COMBINED_LIST)
print("")

# Replicating a list.
print(">> Replicating the list: " + str(LIST_3))
REPLICATED_LIST = LIST_3 * 4
print(REPLICATED_LIST)
print("")

# Deleting items from a list.
print(">> Deleting items from the list: " + str(LIST))
del LIST[1], LIST[2]
print(LIST)
print("")
