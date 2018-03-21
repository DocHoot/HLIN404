#!/usr/bin/env python3

import sys
from Bio import Entrez
from Bio import SeqIO	

ma_db = sys.argv[1]
mon_orgn = sys.argv[2]

Entrez.email = "oscar.main@etu.umontpellier.fr"

ma_req = Entrez.esearch(db=ma_db,retmax=15,term=mon_orgn+"[ORGN] AND "+mon_gene+"[GENE]")

mon_res = Entrez.read(ma_req)
print(mon_res)			#Type de cet objet:
print(mon_res.values())
print(mon_res["Count"])
print(mon_res["IdList"])
ma_req.close()
#----------------------------------------------------------------------------------------------


list_id = mon_res["IdList"]
fic_seq = Entrez.efetch(db="Protein",id=list_id,rettype="gb")
#récupération du résultat
mes_seq = SeqIO.parse(fic_seq,"genbank")
for seq in mes_seq:
	print("sequence ",seq.name," de longueur ",len(seq.seq))
fic_seq.close()