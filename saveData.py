import pprint

data = {
    "name": "Monika",
    "skills": ["Python", "CMD", "Files"],
    "year": 2026
}

file = open("data.py", "w")
file.write("data = ")
file.write(pprint.pformat(data))
file.close()
