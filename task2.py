file = open("Task2_","w")
file.write("I am learning python and I am consistent in it")
file.close()

file = open("Task2_","r")
content = file.read()
print(content)
file.close()