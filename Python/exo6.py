#!/usr/bin/env python3

seq_nuc = "TCTGTTAACCATCCACTTCG"

substitutions = {"A": "T", "T": "A", "C": "G", "G": "C"}

answer = ''

for char in seq_nuc:
	answer += substitutions[char]

print(answer)
