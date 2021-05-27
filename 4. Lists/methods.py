GREETINGS = ["Hi", "Hello", "Hola", "Hey", "Howdy"]

# Finding an item in the list and returning its index.
print("Finding the index of 'Hola' in " + str(GREETINGS) + ".")
print(">> " + str(GREETINGS.index("Hola")))
print("")

GREETINGS = ["Hola", "Hello", "Hola", "Hey", "Howdy", "Hi"]

# Finding an item (with duplicates) in the list and returning its index.
print("Finding the index of 'Hola' (with duplicates) in " + str(GREETINGS) +
      ". The index of the first 'Hola' is ascending order is returned.")
print(">> " + str(GREETINGS.index("Hola")))
print("")

# Adding items to the list.
print("Adding item 'Bonjour' to the list.")
print(">> List before: " + str(GREETINGS))
GREETINGS.append("Bonjour")
print(">> List after: " + str(GREETINGS))
print("")

# Replacing items in the list.
print("Replacing 'Hola' with 'Salut' in the list.")
print(">> List before: " + str(GREETINGS))
GREETINGS.insert(0, "Salut")
print(">> List after: " + str(GREETINGS))
print("")

# Removing items in the list.
print("Removing 'Salut' from the list")
print(">> List before: " + str(GREETINGS))
GREETINGS.remove("Salut")
print(">> List after: " + str(GREETINGS))
print("")

NUMBERS = [1, 3, 6, 0, 2, 5, 3, 2, 8, 3, 11, 24, 23, 14, 4, 6, 7]

# Sorting lists.
print("Sorting the list: " + str(GREETINGS) + " in both ascending and descending alphabetical order.")
GREETINGS.sort()
print(">> " + str(GREETINGS))
GREETINGS.sort(reverse = True)
print(">> " + str(GREETINGS))
print("")

print("Sorting the list: " + str(NUMBERS) + " in both ascending and descending order.")
NUMBERS.sort()
print(">> " + str(NUMBERS))
NUMBERS.sort(reverse = True)
print(">> " + str(NUMBERS))
