#!/usr/bin/env python3
#Import section.
import sys
from Bio import Entrez
from Bio import SeqIO

#Help/Error section.

if len(sys.argv) == 1:
	sys.exit("Error: An argument are required after the program launch! Type -h for help.")
if sys.argv[1] == "-h":
	sys.exit("This program takes a first argument in which you identify the db argument, a second argument in which you give the term search argument, and then a third argument in which you specify the rettype format you wish and finally a fourth argument where you specify the result file location on your computer.")
while len(sys.argv) != 5:
	if len(sys.argv) == 5:
		break
	sys.exit("ERROR: 4 arguments are required after the program launch! Type -h for help.")

##################################################################################################################

Entrez.email = "oscar.main@etu.umontpellier.fr"

ma_req = Entrez.esearch(db=sys.argv[1],retmax=10,term=sys.argv[2])

mon_res = Entrez.read(ma_req)
print(mon_res)			#Type de cet objet:
print(mon_res["Count"])
print(mon_res["IdList"])
ma_req.close()

list_id = mon_res["IdList"]
fic_seq = Entrez.efetch(db=sys.argv[1],id=list_id,rettype=sys.argv[3])
#récupération du résultat
mes_seq = SeqIO.parse(fic_seq,sys.argv[3])
SeqIO.write(mes_seq,sys.argv[4],sys.argv[3])
fic_seq.close()