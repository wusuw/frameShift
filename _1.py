# Author: shunkai chen 
# Date: 2020-08-17 11:27:29 
# Last Modified by:   shunkai chen 
# Last Modified time: 2020-08-17 11:27:29  
# describe:找到相同密码子的个数统计并且找到基因


import sys
import re

def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]

def translate_dna(sequence):
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
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'
    }
    codons = [] # Create a codon list to store codons generated from coding seq.
    for i in range(len(sequence)//3):
        if sequence[3*i:3*i+3] in codontable.keys():
            codons.append(sequence[3*i:3*i+3])
    protein_sequence = ''.join([codontable[codon] for codon in codons]) #Translate condons to protein seq.
    return(protein_sequence)

def main(filein,filein2,fileout):
    f1 = open(filein,"r")       # cds文件
    f2 = open(filein2,"r")      # pep文件
    fo = open(fileout,"w")      # 输出文件
    dic_rna_name_seq = {}
    dic_pep_name_seq = {}
    lis_zimu = []
    for letter in range(65,91):
        lis_zimu.append(chr(letter))
    for line in f1 :      #构建基因组mRNA表
        line = line.strip() 
        if ">" in line :
            b = "_".join(line.split("_")[0:3])
            continue
        else:
            line = line[100:-100]
            dic_rna_name_seq[b] = line
    for lin in f2 :      #构建基因组pep表
        lin = lin.strip() 
        if ">" in lin :
            c = lin.strip().split("_")
            d = "_".join(c[0:3])
            continue
        else:
            lin = lin
            dic_pep_name_seq[d] = lin
    for k,v in dic_pep_name_seq.items():
        for ke,va in dic_rna_name_seq.items():
            if ke == k :
                for i in lis_zimu :
                    rejuzi = re.finditer(str(i)+'{2,50}',v)
                    for j in rejuzi:
                        aa = str(j).split("'")[-2]
                        pos = j.span()
                        start = pos[0]
                        end = pos[1]
                        codon_seq_ = va[3*start:3*end]
                        codon_seq = cut(codon_seq_,3)
                        if len(set(codon_seq)) == 1 :
                            fo.write("\t".join([ke,str(start),str(end),aa,codon_seq_])+"\n")
            else:
                continue
    fo.close()

main(sys.argv[1],sys.argv[2],sys.argv[3])
