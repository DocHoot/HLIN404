#!/usr/bin/env python3
import sys #To allow usage from the linux shell.
import string #In order to allow the use of maketrans and translate.

if (sys.argv[1]=="-h"):   #Error messaging: needs modification.
	print("usage: exo6 ADN(str) nombre(int)")
if(len(sys.argv)!=2):			#2 arguments here: one is used for ./Pyth... and the other is used to give the actual DNA strand.
	print("Error: please give 2 arguments (the program call and the actual DNA strand).")

print(sys.argv[1].translate(str.maketrans('ATGC', 'TACG'))) #Final program output.