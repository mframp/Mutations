import sys

# group with 30
group1 = 'p.Gly12Cys'
# group with 15
group2 = 'p.Gly12Val'
mutName = "KRAS"

inExpFile = open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM.txt", "r")
resultFile = open("outfile_" + mutName + ".txt", "r")

patientsMut1 = []
patientsMut2 = []
matches = []

for line in resultFile:
	line = line.strip().split('\t')
	mut1 = mutName + "_" + group1
	mut2 = mutName + "_" + group2
	# Check patient ids, save if match
	if line[1] == mut1:
		patientsMut1.append(line[0])
	elif line[1] == mut2:
		patientsMut2.append(line[0])

firstLine = inExpFile.readline()
patients = firstLine.strip().split('\t')

match1 = 0
match2 = 0

for patient in patients:
	patient = patient[0:12]
	if patient in patientsMut1:
		match1 += 1
		matches.append(group1)
	elif patient in patientsMut2:
		match2 += 1
		matches.append(group2)
	else:
		matches.append("")

print match1
print match2


#append line to file
with open("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM.txt", "a") as expData:
	expData.write("Class\t")
	for match in matches:
		expData.write(match + '\t')

