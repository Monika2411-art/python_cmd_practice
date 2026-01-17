
file = open("matlibs.txt")
text = file.read()
print(text)

adjective1 = input("Enter an adjective: ")
Noun = input("Enter a noun to replace:  ")
verb = input("Enter a verb to replace : ")
Noun2 = input("Enter 2nd noun to replace: ")

text = text.replace("ADJECTIVE",adjective1)
text = text.replace("NOUN",Noun)
text = text.replace("VERB",verb)
text = text.replace("NOUN",Noun2)

output = open("madlibs_result.txt", "w")
output.write(text)
file.close()

print("Mad Libs story saved to madlibs_result.txt")
