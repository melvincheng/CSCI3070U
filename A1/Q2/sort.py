import random
import matplotlib.pyplot as plt
import sys
import time

array = []
tempArray = []
mergeResult = []
quickResult = []
radixResult = []


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

def mergesort(array):
	length = len(array)
	if length <= 1:
		return array
	else:
		array1 = mergesort(array[:length/2])
		array2 = mergesort(array[length/2:])
		return merge(array1,array2)

def quicksort(array, p, r):
	if p < r:
		k = partition(array, p, r)
		if (k-1 - p < r - k+1 ):
			quicksort(array, p, k-1)
			quicksort(array, k+1, r)
		else:
			quicksort(array, k+1, r)
			quicksort(array, p, k-1)

def partition(array, p, r):
	x = array[r]
	i = p - 1
	for j in range(p, r):
		if array[j] <= x:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[r] = array[r], array[i+1]
	return i+1

def current_milli_time():
	return int(round(time.time() * 1000))

def radix2(num):
    return "{0:b}".format(num)

def digit(num, i):
    x = radix2(num)
    if i >= len(x):
        return 0
    else:
        d = x[-(i+1)]
        return 0 if d == '0' else 1

def COUNTING_SORT(A, i):
    n = len(A)
    k = 2
    B = empty_array(size=n)
    C = empty_array(size=k, init=0)

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

def RADIX_SORT(A):
    n = max(len(radix2(x)) for x in A)
    for i in range(n):
        A = COUNTING_SORT(A, i)
    return A

def generateArray():
	for i in range(100000):
		newString = ""
		for j in range (100):
			# newString += chr(random.randint(32,127))
			newString += chr(random.randint(97,122))
		array.append(newString)




generateArray()
# for x in range (100):
# 	currTime = current_milli_time()
# 	mergeArray = mergesort(array)
# 	mergeResult.append(current_milli_time() - currTime)

for x in range (100):
	# tempArray = array
	currTime = current_milli_time()
	quicksort(array,len(array)/2,len(array)-1)
	quickResult.append(current_milli_time() - currTime)
	print(x)

# print(mergeResult)
print(quickResult)
# print(array)
# for x in range (1):
# 	currTime = current_milli_time()
# 	radixArray = RADIX_SORT(array)
# 	radixResult.append(current_milli_time() - currTime)
# print(radixArray)
	