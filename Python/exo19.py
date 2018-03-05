#!/usr/bin/env python

import sys

			#Error section.

if len(sys.argv) == 1:
	sys.exit("Error: An argument are required after the program launch! Type -h for help.")
if sys.argv[1] == "-h":
	sys.exit("This program takes a file containing Genbank format sequences as the first argument and returns a second file containing the length of each sequence.")
while len(sys.argv) != 2:
	if len(sys.argv) == 2:
		break
	sys.exit("ERROR: An argument is required after the program launch! Type -h for help.")

from Bio import SeqIO
for seq_record in SeqIO.parse(sys.argv[1], 'genbank'):
	print("La sequence " + (seq_record.id) + " a pour longueur " + str(len(seq_record)) + ".")