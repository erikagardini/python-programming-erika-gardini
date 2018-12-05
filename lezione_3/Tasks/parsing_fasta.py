fasta = open("SingleSeq.fasta")

for line in fasta:
	if line[0] == ">":
		print(line)
