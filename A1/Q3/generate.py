import random
file = open("unsorted.txt",'w')
for i in range(100000000):
	print(i)
	newString = ""
	for j in range (100):
		newString += chr(random.randint(32,127))
	file.write(newString+"\n")
file.close()