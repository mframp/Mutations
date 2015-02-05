import sys
from itertools import izip


# inFile1 = open("rtest.txt", "r")
# inFile2 = open("rtest2.txt", "r")
# outFile = open("rtest_outfile.txt", "w")
inFile1 = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_EGFRoutfile.txt", "r")
inFile2 = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_KRASoutfile.txt", "r")
outFile = open("GSM1536837_TCGA_20_joined_outfile.txt", "w")

headerItems = []
headers = inFile1.readline().strip().replace("Missense_Mutation_","").split('\t')
for head in headers:
	headerItems.append(head)

headers2 = inFile2.readline().strip().replace("Missense_Mutation_","").split('\t')
for head in headers2:
	headerItems.append(head)

# Write header line	
print len(headerItems)
outFile.write("\t".join(headerItems) + '\n')

size = 0
for lineFile1, lineFile2 in izip(inFile1, inFile2):
	lineFile2 = lineFile2.strip().split('\t')
	lineFile1 = lineFile1.strip().split('\t')
	del lineFile2[0]
	size = len(lineFile2) + len(lineFile1)
	outFile.write("\t".join(lineFile1) + '\t')
	outFile.write("\t".join(lineFile2) + '\n')

print "size:" + str(size)