# scores=[45,67,89]
# scores.append(75)
# scores.insert(1,60)
# scores[2]=70
# scores[-1]+=5
# scores.pop(0)
# for i in range(len(scores)):
#     print(scores[i])
"""
Tasks:
Create a dictionary called inventory with the following key-value pairs:
{"apple": 10, "banana": 5, "orange": 7}

Add a new item "grape" with quantity 12.
Update the quantity of "banana" to 8.
Increase the quantity of "apple" by 5.
Delete the "orange" entry from the dictionary.
Use a loop to print only the item names.
Use another loop to print only the quantities.
Use a loop to print item names and their quantities (e.g., apple - 15).
"""

inventory={"apple": 10, "banana": 5, "orange": 7}
inventory.update({"grape":12})
inventory.update({"banana":8})
inventory.update({"apple":5})
del(inventory["orange"])
for i in inventory:
    print(inventory[i])
for i in inventory:
    print(i)
for i in inventory:
    print(i,inventory[i])