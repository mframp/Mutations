import sys

inAnnFile = open("PANCAN_Cleaned_Filtered_Annotated.maf", "r")
inMutFile =  open("PANCAN_Mutation_CancerTypes.txt", "r")
outFile = open("outfile_EGFR.txt", "w")

# set up dict
refs = {}
patients = {}

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
				refs[line[CONST_CODE][0:12]] = line[CONST_GENE]

# function to idenify patient_codes with LUAD (lung adenocarcinoma)
def match(cancerType):
	for line in inMutFile:
		line = line.strip().split('\t')
		if line[1] == cancerType:
			code = line[0][0:12]
			if code in refs:
				patients[code] = refs[code]



# call functions
identify("EGFR")
match("LUAD")

# write results to file
for key,val in patients.iteritems():
	outFile.write(key + "\t" + val + '\n')
outFile.close()
