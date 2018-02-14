#!/usr/bin/env python3

import sys

note1 = sys.argv[1]
note2 = sys.argv[2]
note3 = sys.argv[3]

moy = (int(note1)+int(note2)+int(note3))/3

print("La moyenne est ",moy)
