#!/usr/bin/env python3

seq_a = "ATTTTA"
seq_b = "ATTGGA"


def sequence_compare(seq_a, seq_b):
    n = 0
    len1 = len(seq_a)
    len2 = len(seq_b)
    for pos in range(0, min(len1, len2)):
        if seq_a[pos] != seq_b[pos]:
            n = n+1
    return n
      
res = sequence_compare(seq_a, seq_b)
print(res)
