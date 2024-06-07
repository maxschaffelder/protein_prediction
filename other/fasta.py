import numpy as np 
fasta=[]
f = open("pdb_seqres.txt")
for i in f:
   if i[0]=='>':
      count = 1
      header = i[1:-1]

   else:
      seq = i[:-1]
      count = 0

   if count == 0:
     fasta.append((header, seq))
sequences=[]     
print("Merging all records")
for i in fasta:
    for j in i[1]:
       sequences.append(j)
print("Done")
import matplotlib.pyplot as plt
labels, counts = np.unique(sequences,return_counts=True)
ticks = range(len(counts))
plt.bar(ticks,counts, align='center')
plt.xticks(ticks, labels)
plt.show()
#print(fasta[1]) 
