import sys

mutName = "KRAS"

inAnnFile = open("PANCAN_Cleaned_Filtered_Annotated.maf", "r")
# inAnnFile = open("test_input.txt", "r")
inMutFile =  open("PANCAN_Mutation_CancerTypes.txt", "r")
# inMutFile =  open("test_CancerTypes_input.txt", "r")
outFile = open("outfile_" + mutName + ".txt", "w")
analyticsFile = open("analyze_outfile_" + mutName + ".txt", "w")

# set up dict
patients = {}
mutatedMaf = {}
mutatedCancerTypes = {}
mutations = {}

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
				# If patient had LUAD in other file 
				if code in patients:
					# Test for multiple mutations in one patient
					if patients[code] == 'NA':				 
						patients[code] = line[CONST_GENE] + "\t"
					else:
						patients[code] += line[CONST_GENE] + "\t"
					# Dict to keep track of mutation occurances (p.Gys6Leu => 1)
					if line[CONST_GENE] in mutations:
						mutations[line[CONST_GENE]] += 1
					else:
						mutations[line[CONST_GENE]] = 1

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
identify(mutName)
analyze()

# write data to file
#patients = sorted(patients.values())
muts = ''
for key,val in patients.iteritems():
	if val == 'NA':
		outFile.write(key + "\t" + val + '\n')
	else:
		muts += key + "\t" + mutName + "_" + val + '\n'
outFile.write(muts)
outFile.close()

# write analytics file
none = len(patients) - len(mutatedMaf) - len(mutatedCancerTypes)
analyticsFile.write("Total Patients: " + str(len(patients)) + '\n')
analyticsFile.write("Patients with " + mutName + " mutation and LUAD : " + str(len(mutatedCancerTypes)) + '\n')
analyticsFile.write("Patients without a(n) " + mutName + " mutation and LUAD: " + str(none) + '\n\n')
for key,val in mutations.iteritems():
	analyticsFile.write(mutName + "_" + key + "\t" +  str(val) + '\n')
analyticsFile.close()


