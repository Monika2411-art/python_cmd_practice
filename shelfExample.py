import shelve

shelf = shelve.open("mydata")

shelf["name"] = "Monika"
shelf["goal"] = "Successful and happy"
shelf["year"] = 2026

shelf.close()
