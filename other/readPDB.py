import sys
from Bio.PDB import *

filename = sys.argv[1]
p = PDBParser()
structure = p.get_structure("X", filename)
residues =[]
atoms_n = []
atoms_o = []
for model in structure:
     for chain in model:
         for residue in chain:
             for atom in residue:
                if atom.get_name()=='N':
                    atoms_n.append(atom)
                if atom.get_name()=="O":
                    atoms_o.append(atom)

distances = []
for i in range(0, len(atoms_o), 3):
    try:
        distances.append(atoms_o[i]-atoms_n[i+3])
    except:
        pass

dist_ind = []
for i in range(len(distances)):
    if distances[i] > 1.59 and distances[i] < 3.99:
        dist_ind.append(i)

#helix_count = 0
#for i in range(dist_ind):
##    while

print(dist_ind)



# model = structure[0]
# chain = model["A"]
# for i in range(5):
#     print(chain[i]['O']-chain[i+4]['O'])
