from Bio import SeqIO
import re
import numpy as np
import pandas as pd
from itertools import product

def load_sequences(file_path):
    seqs = []
    classes = []
    for record in SeqIO.parse(file_path, "fasta"):
        header = record.description
        seq = str(record.seq).upper()
        match = re.search(r" ([a-z]\.\d+\.\d+\.\d+)", header)
        classe = match.group(1) if match else "unk"
        seqs.append(seq)
        classes.append(classe)
    return seqs, classes

#gera matrix binaria de kmers com skip
def generate_kmer_matrix(seqs):
    aa = list("ACDEFGHIKLMNPQRSTVWY")
    kmers = []
    for a1, a2 in product(aa, repeat=2):
        kmers.append(a1 + a2)
    data = []
    for s in seqs:
        s_pairs = set()
        for i in range(len(s) - 1):
            #skipa 0
            pair = s[i] + s[i+1]
            s_pairs.add(pair)
            #skipa 1
            if i + 2 < len(s):
                pair2 = s[i] + s[i+2]
                s_pairs.add(pair2)
        row = [1 if kmer in s_pairs else 0 for kmer in kmers]
        data.append(row)
    df = pd.DataFrame(data, columns=kmers)
    return df