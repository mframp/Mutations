

data = read.table("GSM1536837_TCGA_20_joined_outfile.txt", header=TRUE, sep="\t",
			 dec=".", row.names=1)
hc = hclust(dist(t(data)))
pdf("KRAS_EGFR.pdf", height=20, width=12)
plot(hc)
graphics.off()