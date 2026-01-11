import shelve 
shelf = shelve.open("mydata")
print(shelf["name"])
print(shelf["goal"])
print(shelf["year"])

shelf.close()
