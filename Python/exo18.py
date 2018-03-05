#!/usr/bin/env python

import sys

		#Debugging.

if len(sys.argv) == 1:
	sys.exit("Error: Two arguments are required after the program launch! Type -h for help.")
if sys.argv[1] == "-h":
	sys.exit("This program takes a file containing Genbank format sequences as the first argument and returns a second file containing the sequences converted to fasta format. The first argument has to be in the genbank format.")
while len(sys.argv) != 3:
	if len(sys.argv) == 3:
		break
	sys.exit("ERROR: Two arguments are required after the program launch! Type -h for help.")

from Bio import SeqIO
nb = SeqIO.convert(sys.argv[1], 'genbank', sys.argv[2], 'fasta')
print(nb)