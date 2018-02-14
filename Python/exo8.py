#!/usr/bin/env python

import re

string = "TCTGTTATGACCATCCACTTCG"

regexp = re.compile(r'ATG')
if regexp.search(string):
	print 'Oui'
else:
	print 'Non'