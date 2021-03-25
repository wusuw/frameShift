# use this file to copy file form result from maxquant
for i in {1..28}
do
	cp SecondInstrument_Sample$i/combined/txt/evidence.txt ./shift4_evidence
	mv shift4_evidence/evidence.txt shift4_evidence/SecondInstrument_Sample$i.txt
done


for i in {10..28}
do
	cp Instrument1_sample$i/combined/txt/evidence.txt ./shift4_evidence
 	mv shift4_evidence/evidence.txt shift4_evidence/Instrument1_sample$i.txt
done


for i in {1..9}
do
	cp Instrument1_sample0$i/combined/txt/evidence.txt ./shift4_evidence
 	mv shift4_evidence/evidence.txt shift4_evidence/Instrument1_sample$i.txt
done
