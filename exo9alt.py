#!/usr/bin/env python3

import sys      #For the sys.argv instances.

seq_a = sys.argv[1]
seq_b = sys.argv[2]

matches = sum(x==y for x,y in zip(seq_a, seq_b))

print("Il y a " + str(matches) + " résidus identiques.")
#This program prints the sum of the differences resulting from the zip command.
#The zip command goes about making "couples" with the position from each list, so [(A,A),[A,T]) and provides the number of matches.
