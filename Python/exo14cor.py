#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
	sys.exit("ERROR: Two arguments are required!")

ficIn = sys.argv[1]
ficOut = sys.argv[2]

i=1
with open(ficIn, "r") as fd:
	with open(ficOut, "w") as fd2:
		for ligne in fd:
			if ligne[0]==">":
				maListe = ligne.split("|")
				maChaine = "seq "+str(i)+" => num gi : "+maListe[1]+", num accession : " + maListe[3]+" \n"
				fd2.write(maChaine)
				i=i+1

fd.close()
fd2.close()