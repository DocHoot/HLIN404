#!/usr/bin/env python3

import sys      #For the sys.argv instances.

seq_a = sys.argv[1]
seq_b = sys.argv[2]

print("La séquence A a " + str(len(seq_a)) + " nucléotides, la séquence B en a " + str(len(seq_b)) + ".")

matches = sum(x==y for x,y in zip(seq_a, seq_b))

print("Il y a " + str(matches) + " résidus identiques entre les 2 séquences.")
#This program prints the sum of the differences resulting from the zip command.
#The zip command goes about making "couples" with the position from each list, so [(A,A),[A,T]) and provides the number of matches.

print("Le pourcentage d'identité est " + str(matches/(len(seq_a + seq_b)/2)*100) + "%.")
