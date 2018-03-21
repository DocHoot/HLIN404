#!/usr/bin/env python3

from Bio import Entrez
from Bio import SeqIO	

Entrez.email = "oscar.main@etu.umontpellier.fr"

ma_req = Entrez.esearch(db="Protein",retmax=10,term="Homo Sapiens[Orgn] AND SRY[gene]")

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
SeqIO.write(mes_seq,"out.fasta","genbank")
fic_seq.close()