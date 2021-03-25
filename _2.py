# Author: shunkai chen 
# Date: 2020-08-14 00:26:10 
# Last Modified by:   shunkai chen 
# Last Modified time: 2020-08-14 00:26:10  
# describe:统计
 

import sys


def main(filein,fileout) : 
    f1 = open(filein,"r")   # hg38_all_identical_codon
    fo = open(fileout,"w")  # out2
    codontable = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 
        'TGC': 'C', 'TGT': 'C', 'TGG': 'W'
    }
    name_locals = locals()
    for i in range(2,50):
        name_locals["list_"+str(i)] = []
        name_locals["dic_"+str(i)] = {}
    for line in f1 : 
        seq = line.split("\t")
        aaa =seq[3]
        aa = seq[3][0]
        codon_seq =seq[4]
        a = len(aaa)
        for j in range(a):
            codon = codon_seq[3*j:3*j+3]
            name_locals['list_'+str(a)].append(aa+"_"+codon)
    for r in range(2,50):
        for o in name_locals['list_'+str(r)] :
            name_locals["dic_"+str(r)][o] = name_locals["dic_"+str(r)].get(o,0)+1
        for ke,va in  codontable.items():
            if va+"_"+ke not in name_locals["dic_"+str(r)].keys():
                name_locals["dic_"+str(r)][va+"_"+ke] = str(0)
            else:
                continue
    for e in range(2,50):
        for k,v in name_locals["dic_"+str(e)].items():
            fo.write("\t".join([str(e),k,str(int(v)/e)])+"\n")
main(sys.argv[1],sys.argv[2])
