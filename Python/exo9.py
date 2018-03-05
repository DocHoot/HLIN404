#!/usr/bin/env python3

import sys

#This is the help section.
if sys.argv[1] == "-h":
    sys.exit("This program takes two nucleotide sequences and prints out the number of identical matches between the two.")
while len(sys.argv) != 3:
	if len(sys.argv) == 3:
		break
	sys.exit("Error: two nucleotidic sequences are required to launch this program.")

seq_a = sys.argv[1]
seq_b = sys.argv[2]

print("La séquence A a " + str(len(seq_a)) + " nucléotides, la séquence B en a " + str(len(seq_b)) + ".")
    
#This is the actual comparing section.
    

def sequence_compare(seq_a, seq_b):
    n = 0
    len1 = len(seq_a)       #Length of the 1st sequence.
    len2 = len(seq_b)       #Length of the 2nd sequence.
    for pos in range(0, min(len1, len2)):       #Estalibhes a for program in relation to the position of arguments in the sequences.
        if seq_a[pos] == seq_b[pos]:        #Checks if the arguments in the same position of each sequence are the same.
            n = n+1         #Adds 1 to the value of n if the two nucleotides are not the same.
    return n
      
res = sequence_compare(seq_a, seq_b)
print("Il y a " + str(res) + " résidus identiques entre les 2 séquences.")      #Number of identical nucleotides between the two genes.
print("Le pourcentage d'identité est " + str(res/(len(seq_a + seq_b)/2)*100) + "%.")