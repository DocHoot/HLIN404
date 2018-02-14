#!/usr/bin/env python

while True:
   print "Who are you?" #remember to use the print command without parenthesis in python 2.7 although it is completely required in python 3.
   name = raw_input() #using raw_imput() in python 2.7 seems to be required, although just using input() seems to be more than sufficient in python3.
   if name != 'Joe':
       continue
   print "Hello Joe. What is the password?"
   password = raw_input()
   if password == "swordfish":
       break
print "Access granted."
