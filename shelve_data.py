import shelve
shelf = shelve.open("MYshelf")
shelf["name"] = "Monika"
shelf["skills"] = ["Python", "CMD", "File Handling"]
shelf["goal"] = "Automation Engineer"

shelf.close()

print("Data saved successfully")