import math
import sys
import random

import matplotlib.pyplot as plt
import numpy as np

def main():

	if(len(sys.argv) < 5):
		print "Usage: N m hash-func plot-file"
		return
	else:
		# Check is N and m are integers
		try:
			N = int(sys.argv[1])
			m = int(sys.argv[2])
		except:
			print "N and m must be integers"
			return

	inFunc = sys.argv[3]

	# determines which function is going to be used
	if(inFunc == "f1"):
		func = lambda k, m: k**2%m
	elif(inFunc == "f2"):
		func = lambda k, m: int(math.floor((0.2 * (k % 1000000.0) - math.floor(0.2 * (k % 1000000.0))) * m))
	elif(inFunc == "f3"):
		func = lambda k, m: int(math.floor((0.618034 * (k % 1000000.0) - math.floor(0.618034 * (k % 1000000.0))) * m))
	elif(inFunc == "f4"):
		func = lambda k, m: int(math.floor((0.8 * (k % 1000000.0) - math.floor(0.8 * (k % 1000000.0))) * m))
	else:
		print "Invalid hash function"
		return

	# initialize the hashmap
	hashMap = [[] for i in range(m)]


	# fills map
	for i in range(N):
		x = random.randint(0, sys.maxint)
		k = func(x, m)
		hashMap[k].append(x)

	print "Longest collision:", len(max(hashMap, key=len))
	# x axis range
	count = [len(hashMap[i]) for i in range(m)]

	# calculates the y axis increments
	y_pos = np.arange(m)

	# plots graph
	plt.bar(y_pos, count)
	plt.ylabel("Collisions")
	plt.xlabel("Slot")
	plt.xlim(0,m)
	plt.title("Collisions per slot (N = " + str(N) + ", m = " + str(m) + ", function = " + inFunc + ")")

	plt.savefig(sys.argv[4])

main()