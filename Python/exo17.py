#!/usr/bin/env python3

dico_espece = {'Escherichia coli':3.6,'Homo sapiens':3200,'Saccharomyces cerevisae':12,'Arabidopsis thaliana':125}

maximum = max(dico_espece, key=dico_espece.get)
print(maximum, dico_espece[maximum])