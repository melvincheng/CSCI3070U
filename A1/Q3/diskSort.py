import sys
import os
import time

# Gets current time in milliseconds
def current_milli_time():
	return int(round(time.time() * 1000))

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

# Reads in a part of the file, also determines if the file is at EOF
def chunk(file, array):
	full = False
	while(not full):
		read = file.readline()
		array.append(read)
		# os.stat('fileName').st_size gets the file size
		# after getting file size, divide it by 1000 so that files are approximately 1000th the size of the original file
		# checks if at EOF
		if(sys.getsizeof(array) > os.stat('unsorted.txt').st_size / 1000 or read == ''):
			full = True
	if(read == ''):
		return False
	return True

def main():
	tempArray = []
	oldFile = open('unsorted.txt', 'r')
	# used as the chunks' file name
	fileNum = 0
	check = True

	# Splits the data into chunks and sorts the individual chunks
	while(check):
		check = chunk(oldFile, tempArray)
		# quicksort(tempArray, 0, len(tempArray) - 1)
		tempArray = mergesort(tempArray)
		newFile = open(str(fileNum),'w')
		fileNum += 1
		for x in tempArray:
			newFile.write(x)
		newFile.close()
		#empties array to save memory
		tempArray = []

	oldFile.close()

	# used to store data from each file
	tempArray = []
	# array used to store and access the sorted chunk files
	chunkFiles = []
	sortedFile = open('sorted.txt','w')
	# opening and storing the chunk files into the chunkFiles array
	for x in range (fileNum):
		tempFile = open(str(x), 'r')
		chunkFiles.append(tempFile)
		tempArray.append(chunkFiles[x].readline())
	# merges all the files into one sorted file
	while(True):
		sortedFile.write(min(tempArray))
		# file the index of the element that was just written to the file so the next line can be read
		minIndex = tempArray.index(min(tempArray))
		# reads in the next
		tempArray[minIndex] = chunkFiles[minIndex].readline()
		# checks if the file that was just pushed is at EOF
		# if so the file is closed and the index is removed from both the chunkFiles array and array containing the data and everything is shifted back
		if(tempArray[minIndex] == ''):
			emptyInd = tempArray.index('')
			del tempArray[emptyInd]
			chunkFiles[emptyInd].close()
			del chunkFiles[emptyInd]
		# no more elements remain, then end loop
		if(len(tempArray) == 0):
			break
	# delete all the chunk files created
	for x in range (fileNum):
		os.remove(str(x))

currTime = current_milli_time()
main()
print "Done: It took", current_milli_time() - currTime, "millisecond(s) to complete"

# TEST CODE TO MAKE SURE SORTING IS CORRECT
# array = []
# file = open('newTest.txt', 'r')
# for x in file:
# 	array.append(x)
# quicksort(array,0,len(array)-1)
# file.close()
# file = open('right.txt', 'w')
# for x in array:
# 	file.write(x)