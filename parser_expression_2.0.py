import sys
import time
import argparse

# Parsing the mutation name from command line
parser = argparse.ArgumentParser()
parser.add_argument("geneName", help="Name of the gene for which you want information.", type=str)
args = parser.parse_args()
mutName = args.geneName

inExpressFile = open("/fslhome/srp33/fsl_groups/fslg_piccololab/PANCAN20/GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM.txt", "r")
outFile = open("/fslhome/mframp14/fsl_groups/fslg_piccololab/MFrampton/GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_" + mutName + "outfile.txt", "w")
resultFile = open("/fslhome/mframp14/fsl_groups/fslg_piccololab/MFrampton/outfile_" + mutName + ".txt", "r")

sampleIDs = []
sampleInfo = []

for line in resultFile:
	line = line.strip().split('\t')
	# Save patient ids of those that aren't NA
	if line[1] != 'NA':
		sampleIDs.append(line[0])
		sampleInfo.append('_'.join(line[1::]))


# Split first row of patient ids
headerItems = []
headers = inExpressFile.readline().strip().split('\t')
for head in headers:
	headerItems.append(head[0:12])

# Save indices of patient ids that have a match, as well as 0 to keep row headers
keepSampleIndices = [0]
for index,item in enumerate(headerItems):
	if item in sampleIDs:
		keepSampleIndices.append(index)
		# Write the column headers with format: id_info
		# Note: .index() only returns index of first occurance
		outFile.write(item + '_' + sampleInfo[sampleIDs.index(item)] + "\t")
		print item + '_' + sampleInfo[sampleIDs.index(item)]

# Write newline following column headers
outFile.write('\n')

start = time.clock()
# Write only the columns with the specified indices
for line in inExpressFile:
	lineItems = line.strip().split('\t')
	outItems = [lineItems[i] for i in keepSampleIndices]
	outFile.write("\t".join(outItems) + "\n")

end = time.clock()
print "TIME: " + str(end- start)

