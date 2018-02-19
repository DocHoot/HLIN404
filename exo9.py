#!/usr/bin/env python3

import sys

#This is the help section.
if sys.argv[1] == "-h":
    print("This program takes two nucleotide sequences and prints out the number of identical matches between the two.")
if len(sys.argv) != 3:
    print("Please use two nucleotide sequences.")

seq_a = sys.argv[1]
seq_b = sys.argv[2]
    
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
print(res)      #Number of identical nucleotides between the two genes.
