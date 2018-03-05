#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	sys.exit("ERROR: Three arguments required after the program launch! Type -h for help.")
if sys.argv[1] == "-h":
	sys.exit("Takes an argument with Genbank format sequences and creates two files in return: one returning the inverse complement of the sequences in the fasta format and the other with the protein sequences in the fasta format.")
while len(sys.argv) != 4:
	if len(sys.argv) == 4:
		break
	sys.exit("ERROR: Three arguments are required after the program launch! Type -h for help.")

from Bio import SeqIO
maListeRecord = SeqIO.parse(sys.argv[1], 'genbank')

	#First step: returning a reverse complement of the sequences to the file indicated in the 3rd argument position.
with open(sys.argv[2], 'w') as fd:
	for seq in maListeRecord:
		fd.write(str(seq.reverse_complement('fasta')))

	#Second step: returning the protein translate to the file indicated in the 4th argument position.
with open(sys.argv[3], 'w') as fd2:
	for seq in maListeRecord:
		fd2.write(str(seq.translate('fasta')))

fd.close()		#These 2 close the files.
fd2.close()