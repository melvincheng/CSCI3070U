import random
import matplotlib.pyplot as plt
import sys
import time

# Merge used in merge sort, algorithm used is from the lecture slides
def merge(array1, array2):
	i, j = 0, 0
	array3 = []

	while i < len(array1) and j < len(array2):
		if array1[i] <= array2[j]:
			array3.append(array1[i])
			i += 1
		else:
			array3.append(array2[j])
			j += 1

	if i < len(array1): array3.extend(array1[i:])

	if j < len(array2): array3.extend(array2[j:])

	return array3

# Merge sort, algorithm used is from the lecture slides
def mergesort(array):
	length = len(array)
	if length <= 1:
		return array
	else:
		array1 = mergesort(array[:length/2])
		array2 = mergesort(array[length/2:])
		return merge(array1,array2)

# Tail recursive quicksort, algorithm used is from the textbook
def quicksort(array, p, r):
	while p < r:
		q = partition(array, p, r)
		quicksort(array, p, q - 1)
		p = q + 1

# Partition used in quick sort, algorithm used is from the lecture slides
def partition(array, p, r):
	x = array[r]
	i = p - 1
	for j in range(p, r):
		if array[j] <= x:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[r] = array[r], array[i+1]
	return i+1

# Gets current time in milliseconds
def current_milli_time():
	return int(round(time.time() * 1000))

# changes string to a string binary 
def stringToBin(array):
	for x in range (len(array)):
		array[x] = ' '.join(format(ord(i), 'b') for i in array[x])

# changes a string binary to a string
def binToString(array):
	for x in range (len(array)):
		stringsArray = array[x].split(' ')
		array[x] = ''.join(chr(int(i, 2)) for i in stringsArray)

# digit function used in counting sort, algorithm used is from the lecture slides,
# the code is slightly modified that binary converstion is removed
def digit(num, i):
	x = num
	if i >= len(x):
		return 0
	else:
		d = x[-(i+1)]
		return 0 if d == '0' else 1

# counting sort used in radix sort, algorithm used is from the lecture slides
def COUNTING_SORT(A, i):
	n = len(A)
	k = 2
	B = [None] * n
	C = [0] * k

	for a in A:
		d = digit(a, i)
		C[d] = C[d] + 1

	for j in range(1,k):
		C[j] = C[j] + C[j-1]

	for a in reversed(A):
		d = digit(a, i)
		B[C[d]-1] = a
		C[d] = C[d] - 1

	return B

# radix sort, algorithm used is from the lecture slides,
# the code is slightly modified that the entire array is convert at the beginning and 
# converted back at the end instead of converting during sorting
def RADIX_SORT_STRING(A):
	stringToBin(A)
	n = max(len(x) for x in A)
	for i in range(n):
		A = COUNTING_SORT(A, i)
	binToString(A)
	return A

# used to generate an array with 1000000 strings each 100 characters long
def generateArray():
	array = []
	for i in range(1000000):
		newString = ""
		for j in range (100):
			# newString += chr(random.randint(32,127))
			newString += chr(random.randint(97,122))
		array.append(newString)
		sys.stdout.write("\r%i" % i)
		sys.stdout.flush()
	sys.stdout.write("\rdone generation\n")
	return array

def main():
	tempArray = []
	mergeResult = []
	quickResult = []
	radixResult = []

	newArray = generateArray()
	
	# merge sort
	for x in range (100):
		currTime = current_milli_time()
		mergeArray = mergesort(newArray)
		mergeResult.append(current_milli_time() - currTime)
	print(mergeResult)
	print('Done: merge sort')

	# quick sort
	for x in range (100):
		tempArray = newArray[:]
		currTime = current_milli_time()
		quicksort(tempArray,0,len(tempArray)-1)
		quickResult.append(current_milli_time() - currTime)
	print(quickResult)
	print('Done: quick sort')

	# radix sort
	for x in range (100):
		tempArray = newArray[:]
		currTime = current_milli_time()
		radixArray = RADIX_SORT_STRING(tempArray)
		radixResult.append(current_milli_time() - currTime)
	print(radixResult)
	print('Done: radix sort')

main()
