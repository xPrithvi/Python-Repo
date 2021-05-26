SUPPLIES = ["Pen", "Ruler", "Pencil", "Paper", "Rubber"]

print("Looping over list using the first algorithm: " + str(SUPPLIES))
for i in range(len(SUPPLIES)):
    print("Index: " + str(i) + " Item: " + str(SUPPLIES[i]))
print("")

print("Looping over list using the second algorithm: " + str(SUPPLIES))
index = 0
for item in SUPPLIES:
    print("Index: " + str(index) + " Item: " + item)
    index += 1
