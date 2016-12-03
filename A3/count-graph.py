import sys

edge = 0
vertices = 0

file = open(sys.argv[1], 'r')

subgraphs = []

for line in file:
	temp = line.split('|')
	subgraphs.append([temp[0], temp[1]])

for x in range (len(subgraphs)):
	y = x + 1
	while y < len(subgraphs):
		if(any(i in subgraphs[x] for i in subgraphs[y])):
			edge += list(i in subgraphs[x] for i in subgraphs[y]).count(True)
			subgraphs[x] += subgraphs[y]
			subgraphs.pop(y)
			y = x
		y += 1

for x in subgraphs:
	# print x
	vertices += len(set(x))

print "Number of vertices:", vertices
print "Number of edges:", edge


array1 = [1,0,0,3]
array2 = [1,1,1,2]

print list(i in array1 for i in array2).count(True)