# Author: shunkai chen 
# Date: 2020-09-02 20:17:16 
# Last Modified by:   shunkai chen 
# Last Modified time: 2020-09-02 20:17:16  
# describe:氨基酸的缩写与氨基酸之间的互换
 
import sys 

def main(filein,fileout) : 
    f1 = open(filein,"r") 
    fo = open(fileout,"w")
    dic_aa_a = {"His":"H","Gln":"Q","Arg":"R","Ile":"I","Met":"M",
                "Thr":"T","Asn":"N","Lys":"K","Ser":"S","Val":"V",
                "Ala":"A","Asp":"D","Glu":"E","Gly":"G","Phe":"F",
                "Leu":"L","Tyr":"Y","Cys":"C","Trp":"W","Pro":"P"} 
    lis_aa = ["A","Q","D","P","S","L","E","G","K","H","N","T","I","M","C","R","V","W","F","Y"]
    lis_txt = []
    lis_t = []
    for l in f1:
        lis_t.append(l)
    for i in lis_aa:
        for li in lis_t:
            if i in li:
                lis_txt.append(li)
            else:
                continue
    for line in lis_txt : 
        if line.startswith("AA"):
            continue
        else:
            seq = line.split("\t")
            a = seq[0]
            for k,v in dic_aa_a.items():
                if v == a:
                    aa = k
                    fo.write(aa+"\t"+line)
    fo.close()

main(sys.argv[1],sys.argv[2])
