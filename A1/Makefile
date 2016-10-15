.PHONY: all prepare clean run

all: big wide

big: big.txt sort-strings.py
        python sort-strings.py big.txt

big.txt: make-strings.py
        python make-strings.py 100000 100 big.txt

wide: wide.txt sort-strings.py
        python sort-strings.py wide.txt

wide.txt: make-strings.py
        python make-strings.py 1000 10000 wide.txt
        
clean:
        rm -f *.txt
