import sys

inAnnFile = open("PANCAN_Cleaned_Filtered_Annotated.maf", "r")
# inAnnFile = open("test_input.txt", "r")
inMutFile =  open("PANCAN_Mutation_CancerTypes.txt", "r")
# inMutFile =  open("test_CancerTypes_input.txt", "r")
outFile = open("outfile_EGFR.txt", "w")
analyticsFile = open("analyze_outfile.txt", "w")

# set up dict
patients = {}
mutatedMaf = {}
mutatedCancerTypes = {}

# define constants
CONST_SIFT = 59
CONST_POLY = 60
CONST_NAME = 0
CONST_CODE = 15
CONST_GENE = 35

# function to identify patient_codes where name = KRAS and
# 	SIFT_pred = D and
#	Polyphen2_HVAR_pred = D
def identify(mutation):
	for line in inAnnFile:
		line = line.strip().split('\t')
		if line[CONST_NAME] == mutation:
			if line[CONST_SIFT] == 'D' and line[CONST_POLY] == 'D':
				code = line[CONST_CODE][0:12] 
				if code in patients:				 
					patients[code] = line[CONST_GENE]
				else:
					patients[code] = line[CONST_GENE] + " (FOUND IN .maf BUT NOT cancerTypes.txt)"

# function to idenify patient_codes with LUAD (lung adenocarcinoma)
def match(cancerType):
	for line in inMutFile:
		line = line.strip().split('\t')
		if line[1] == cancerType:
			code = line[0][0:12]
			patients[code] = 'NA'				

# function to analyze data
def analyze():
	for key,val in patients.iteritems():
		if val[-1] == ')':
			mutatedMaf[key] = val
		elif val[0] == 'p':
			mutatedCancerTypes[key] = val



# call functions
match("LUAD")
identify("EGFR")
analyze()

# write data to file
for key,val in patients.iteritems():
	outFile.write(key + "\t" + val + '\n')
outFile.close()

# write analytics file
none = len(patients) - len(mutatedMaf) - len(mutatedCancerTypes)
analyticsFile.write("Total Patients: " + str(len(patients)) + '\n')
analyticsFile.write("Patients with EGFR mutation in CancerTypes.txt: " + str(len(mutatedCancerTypes)) + '\n')
analyticsFile.write("Patients with EGFR mutation in ONLY .maf: " + str(len(mutatedMaf)) + '\n')
analyticsFile.write("Patients without an EGFR mutation: " + str(none) + '\n')
analyticsFile.close()


