import matplotlib.pyplot as plt

def getHydro(seq, KD):
	hydrophobicity = []
	for el in seq:
		hydrophobicity.append(KD.get(el))
	return hydrophobicity

def plotHydro(seq, hydro):
	plt.plot(range(0,len(seq)), hydro)
	plt.title("Hydrophobicity pattern")
	plt.xlabel("residue number")
	plt.ylabel("hydrophobicity")
	plt.show()

def findPattern(pattern, seq):
	return seq.find(pattern)

file = open("file_with_seq.txt", "r")
seq = file.read()

KD = {'A': 1.8, 'C':2.5, 'D': -3.5, 'E': -3.5,
      'F': 2.8, 'G': -0.4, 'H': -3.2, 'I':4.5,
      'K': -3.9, 'L': 3.8,'M':1.9, 'N':-3.5,
      'P':-1.6, 'Q':-3.5, 'R':-4.5, 'S':-0.8,
      'T': -0.7, 'V':4.2, 'W':-0.9, 'Y':-1.3}

hydrophobicity = getHydro(seq, KD)
plotHydro(seq, hydrophobicity)
result = findPattern("AAAFV", seq)
if result != -1:
	print("Pattern trovato! Posizione iniziale: ")
	print(result)
else:
	print("Pattern non trovato")