import sys


file = open(sys.argv[1], 'r')

subgraphs = []

for line in file:
	temp = line.split('|')
	subgraphs.append([temp[0], temp[1]])

for x in range (len(subgraphs)):
	y = x + 1
	while y < len(subgraphs):
		if(any(i in subgraphs[x] for i in subgraphs[y])):
			subgraphs[x] += subgraphs[y]
			subgraphs.pop(y)
			y = x
		y += 1

# total = 0

for x in subgraphs:
	print x
	print len(set(x))
	# total += len(set(x))

# print total

print "Total number of connected components:", len(subgraphs)