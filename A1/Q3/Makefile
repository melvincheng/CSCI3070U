.PHONY: all prepare run clean

all: prepare run

prepare: 
	python make-strings.py 100000000 100 unsorted.txt

run: unsorted.txt diskSort.py
	python diskSort.py

clean:
	rm -f *.txt
