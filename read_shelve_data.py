import shelve
shelf = shelve.open("MYshelf")

print(shelf["name"])
print(shelf["skills"])
print(shelf["goal"])

shelf.close()