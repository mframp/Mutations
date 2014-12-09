import random

# inFile = open("outfile_EGFR_KRAS.txt", "r")
inFile = open("test_random_in.txt", "r")
outTrain = open("test_trainData.txt", "w")
outTest = open("test_testData.txt", "w")

mut1 = "EGFR"
mut2 = "KRAS"

mut1List = []
mut2List = []
naList = []

# Parse file into 3 
for line in inFile:
	line = line.strip()
	lineSplit = line.split('\t')
	if lineSplit[1] == 'NA':
		naList.append(line)
	else:
		protein = lineSplit[1].split('_')
		if protein[0] == mut1:
			mut1List.append(line)
		elif protein[0] == mut2:
			mut2List.append(line)


# Randomly shuffle each list
random.shuffle(mut1List)
random.shuffle(mut2List)
random.shuffle(naList)

# Split into two files
trainData = []
testData = []

halfNa = len(naList)/2
halfMut1 = len(mut1List)/2
halfMut2 = len(mut2List)/2
trainData = naList[halfNa:] + mut1List[halfMut1:] + mut2List[halfMut2:]
testData = naList[:halfNa] + mut1List[:halfMut1] + mut2List[:halfMut2]

for item in trainData:
	outTrain.write(item + "\n")
outTrain.close()
for item in testData:
	outTest.write(item + "\n")
outTest.close()