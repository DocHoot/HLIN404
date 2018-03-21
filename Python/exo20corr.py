#!/usr/bin/env python3

import sys
from Bio import seqIO

if len(sys.argv) == 1:
	sys.exit("ERROR: Three arguments required after the program launch! Type -h for help.")
if sys.argv[1] == "-h":
	sys.exit("Takes an argument with Genbank format sequences and creates two files in return: one returning the inverse complement of the sequences in the fasta format and the other with the protein sequences in the fasta format.")
while len(sys.argv) != 4:
	if len(sys.argv) == 4:
		break
	sys.exit("ERROR: Three arguments are required after the program launch! Type -h for help.")

ficGb = sys.argv[1]
ficRevFasta = sys.argv[2]
ficProtFasta = sys.argv[3]

listeSeqRev = []
#with open(ficRevFasta, 'w') as fd:
for maSeq in SeqIO.parse(ficGb, 'genbank'):
	maSeq.seq=maSeq.seq.reverse_complement()
	#fd.write(maSeq.format('fasta'))
	listeSeqRev.append(maSeq)

SeqIO.write(listeSeqRev,ficRevFastan,'fasta')

listeSeqprot=[]
#with open(ficProtFasta, 'w') as fd2:
for maSeq if SeqIO.parse(ficGb, 'genbank'):
	maSeq.seq=maSeq.seq.translate()
	#fd2.write(maSeq.format('fasta'))
	listeSeqprot.append(maSeq)

SeqIO/write(listeSeqprot,ficProtFasta,'fasta')