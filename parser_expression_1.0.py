import sys

# group with 30
group1 = 'p.Gly12Cys'
# group with 15
group2 = 'p.Gly12Val'
mutName = "KRAS"

inExpFile = open("/fslhome/srp33/fsl_groups/fslg_piccololab/PANCAN20/GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM.txt", "r")
outFile = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_outfile.txt", "w")
resultFile = open("outfile_" + mutName + ".txt", "r")

sampleIDs = []

for line in resultFile:
	line = line.strip().split('\t')
	mut1 = mutName + "_" + group1
	mut2 = mutName + "_" + group2
	# Save patient ids of those that have mutation from type1 or type2
	if line[1] == mut1 or line[1] == mut2:
		sampleIDs.append(line[0])

# Split first row of patient ids
headerItems = inExpFile.readline().strip().split('\t')
# Save indices of patient ids that have a match 
keepSampleIndices = [headerItems.index(sampleID) for sampleID in sampleIDs]
