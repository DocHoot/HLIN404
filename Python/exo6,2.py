#!/usr/bin/env python

import re

seq1 = "ATGCGTAGCGT"
seq2 = "AGGTTCGTATG"
mesSeq = [seq1, seq2]

print("Il  a " + str(len(re.findall("A", mesSeq))) + " nucleotides A")
