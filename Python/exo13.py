#!/usr/bin/env python

import sys

from Bio import SeqIO
for seq_record in SeqIO.parse(sys.argv[1], 'fasta'):
	print(seq_record.id + seq_record.description)