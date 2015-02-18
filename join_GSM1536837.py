import sys
from itertools import izip


# inFile1 = open("rtest.txt", "r")
# inFile2 = open("rtest2.txt", "r")
# outFile = open("rtest_outfile.txt", "w")
# inFile1 = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_EGFRoutfile.txt", "r")
inFile1 = open("GSM1536837_TCGA_20_EGFR_KRAS_BRAF_outfile.txt", "r")
inFile2 = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_TP53outfile.txt", "r")
outFile = open("GSM1536837_TCGA_20_EGFR_KRAS_BRAF_TP53_outfile.txt", "w")

headerItems = []
# patientIDs used to check for duplicate patient ids,
# (patients with mutations in more than one of: KRAS,BRAF,TP53,EGFR)
patientIDs = []

headers = inFile1.readline().strip().split('\t')
for head in headers:
	# patientIDs.append(head[0:12])

	# if TCGA_12_2432_ on front, chop it off
	if len(head) > 16:
		headerItems.append(head[13:])
	else:
		headerItems.append(head)

headers2 = inFile2.readline().strip().split('\t')
for head in headers2:
	# if head[0:12] in patientIDs:
	# 	print head[0:12]
	if len(head) > 16:
		headerItems.append(head[13:])
	else:
		headerItems.append(head)

# DUPLICATES:
# TCGA-21-5787
# TCGA-33-6737

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