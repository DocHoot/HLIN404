#!/usr/bin/env python3

import sys      #For the sys.argv instances.

#This is the help section.
if sys.argv[1] == "-h":
    print("This program takes two nucleotide sequences and prints out the number of identical matches between the two.")
    sys.exit()
while len(sys.argv) != 3:
	if len(sys.argv) == 3:
		break
	print("Error: two nucleotidic sequences are required to launch this program.")
	sys.exit()

seq_a = sys.argv[1]
seq_b = sys.argv[2]

matches = sum(x==y for x,y in zip(seq_a, seq_b))

print("Il y a " + str(matches) + " résidus identiques.")
#This program prints the sum of the differences resulting from the zip command.
#The zip command goes about making "couples" with the position from each list, so [(A,A),[A,T]) and provides the number of matches.
