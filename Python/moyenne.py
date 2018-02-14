#!/usr/bin/env python3

note1 = input("Donner une note : ")
note2 = input("Donner une note : ")
note3 = input("Donner une note : ")

Note1 = int(note1)
Note2 = int(note2)
Note3 = int(note3)

moyenne = (Note1+Note2+Note3)/3
moyennestr = str(moyenne)
print("La moyenne est égale à " + moyennestr)

if 0<moyenne<10:		#I thought it would be possible to do this using a different system yet this method, although long, seems to be the most easy to operate in the long run.
	print("Ajourné.")

if 10<=moyenne<12:
	print("Passable.")

if 12<=moyenne<14:
	print("Assez bien.")

if 14<=moyenne<16:
	print("Bien.")

if 16<=moyenne<20:
	print("Très bien.")