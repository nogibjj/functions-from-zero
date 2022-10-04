# create a list with different types of fruit
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

# loop through the fruits and count the total fruits in the list
for i in fruit:
    # use an f-string to print the fruit name and the number of the fruit in the list
    print(f"{i} is fruit number {fruit.index(i)+1}")

# the total number of fruits in the list
print(f"There are {len(fruit)} fruits in the list")
