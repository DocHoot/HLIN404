#!/usr/bin/env python

import sys
import re

n = 0

for i in sys.argv[1]:
	n = n+1
	str = sys.argv[1]
	search = re.compile(r"^>(.+)\|(.+)\|(.+)\|(.+)\|(.+)$")
file = open(sys.argv[2], "w")
print(search.pattern)