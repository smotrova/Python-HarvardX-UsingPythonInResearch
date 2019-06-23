# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 08:21:36 2018

@author: Olena

week 3 DNA Translation
"""

# Download data
# Import the DNA data into Python
# Create algorithm to translate DNA
# Check if translation matches your downloads

#---------------------------------------------------------

def read_seq(inputfile):
    """ reads and returns the input sequence with special charachters removed """

    with open(inputfile, "r") as f:
        seq = f.read()
    
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    
    return seq


seq = read_seq(".\Data\dna.txt")

type(seq)
len(seq)

def translate(seq):

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    # check the lengtn of the sequence
    # should be devided by 3
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]
            
    return protein

translate("GCC")

translate(seq[20:938])

prt = read_seq(".\Data\protein.txt")

# exclude last character
translate(seq[20:938])[:-1] == prt
