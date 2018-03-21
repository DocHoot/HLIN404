#!/usr/bin/env python3

import sys
from Bio import Entrez
from Bio import SeqIO			#Target document file.

Entrez.email = "oscar.main@etu.umontpellier.fr"
fd = open("exo21.txt", "w+")

with open(sys.argv[1], 'w'):
	handle = Entrez.efetch(db="nuccore", term="SRY[Gene]", rettype="gb", retmax="10")
	records = Entrez.read(handle)
	fd.write(records)