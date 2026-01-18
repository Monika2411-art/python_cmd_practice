import os
import re
pattern = input("Enter regex pattern: ")
files = os.listdir(".")
print(files)

for filename in files:
	if filename.endswith(".txt"):
		file = open(filename)
		content = file.read()
		file.close()
	 
		matches = re.findall(pattern,content)

		if matches:
			print(f"\nMatches in {filename}:")
			for match in matches:
				print(match)