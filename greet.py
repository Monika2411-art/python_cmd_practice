import sys
print("Filename: ",sys.argv[0])
print("Name: " , sys.argv[1])

if len(sys.argv) < 2:
	print("Please provide name")
else:
	print("Hello: ",sys.argv[1]) 