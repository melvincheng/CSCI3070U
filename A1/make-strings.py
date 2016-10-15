import sys
import os
import random

if len(sys.argv) < 4:
    print "Usage: N w f"
    sys.exit(0)

N = int(sys.argv[1])
w = int(sys.argv[2])
filename = sys.argv[3]

def randchr():
    return chr(random.randint(65, 65+26))

def randstr(w):
    return "".join(randchr() for i in range(w))

with open(filename, "w") as f:
    for i in range(N):
        f.write(randstr(w) + "\n")

print "All done with %d strings, saved to %s" % (N, filename)
