


inEGFRFile = open("outfile_EGFR.txt", "r")
# inKRASFile = open("outfile_KRAS.txt", "r")
# outFile = open("outfile_EGFR_KRAS.txt" , "w")

with open("outfile_KRAS.txt") as inFile:
	with open("outfile_EGFR_KRAS", "w") as outFile:
		for line in inFile:
        		outFile.write(line) 