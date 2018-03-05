#!/usr/bin/env python

import sys

from Bio import SeqIO
maSeq = SeqIO.read(sys.argv[1], 'fasta')
print(maSeq)