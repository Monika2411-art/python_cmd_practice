#WITHOUT PPRINT
print("WITHOUT PPRINT")
data = {
	"Name: " : "monika",
	"goal":{
		"Being happy",
		"Be Successful",
		"Be pretty",
		"Be healthiest"}} 
print(data)


import pprint
print()
#WITH PPRINT
print("WITH PPRINT")
print("✅ You can read nested data easily")
data2 = {
	"Name: " : "monika",
	"goal":{
		"Being happy",
		"Be Successful",
		"Be pretty",
		"Be healthiest"}} 
pprint.pprint(data2)



import pprint
#pformat() → returns a nicely formatted STRING
data3 = {
    "name": "Monika",
    "skills": ["Python", "CMD", "File Handling", "Automation"],
    "habits": ["Consistency", "Learning daily", "Discipline"],
    "projects": {
        "current": "Python practice",
        "future": "Web scraping"
    }
}

formatted_data = pprint.pformat(data3)
file = open("pretty_format_output.txt","w")
file.write(formatted_data)
file.close()
print("Data successfully written to pretty_format_output.txt")

