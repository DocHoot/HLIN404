#!/usr/bin/env python3
#Programme qui lance un blast au NCBI d'une sequence requete contre Genbank par ex et d'afficher les numéros
#d'accession des 10 premieres sequences qui matchent avec la sequence requete avec la e-value et le score du
#meilleur HSP de chaque sequence.

from Bio import SeqIO
from Bio import AlignIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

handle= NCBIWWW.qblast("blastp","nr", "gb")
blast_records=NCBIXML.parse(handle)
for record in NCBIXML.parse(handle):
	if record.alignments:
		#Resort using bit score rather than e-value
		record.alignment.sort(key=lambda align: -max(hsp.score for hsp in align.hsps))
		print(record.alignments[0].hit_id)