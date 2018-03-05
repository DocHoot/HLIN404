#!/usr/bin/env python3

seq_nuc = input()

nucleotides = {"A": "pyrimidinique", "T": "pyrimidinique", "C": "purinique", "G": "purinique"}		#Replaces actual string.

answer = ''				#Provides blank slate for the answer.
for char in seq_nuc:			#Identifies character:
	answer += nucleotides[char]		#Actual replacement via use of dictionnary.

print("La base donnée est " + answer + ".")