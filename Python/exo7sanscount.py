#!/usr/bin/env python
# Exercice exo7.py qui n'utilise pas la commande count().
import re
string = "TCTGTTAACCATCCACTTCG"
print("Il y a " + str(len(re.findall("A", string))) + " nucléotides A")
print("Il y a " + str(len(re.findall("T", string))) + " nucléotides T")
print("Il y a " + str(len(re.findall("C", string))) + " nucléotides C")
print("Il y a " + str(len(re.findall("G", string))) + " nucléotides G")