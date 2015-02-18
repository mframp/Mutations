

data = read.table("GSM1536837_TCGA_20_EGFR_KRAS_BRAF_outfile.txt", header=TRUE, sep="\t",
			 dec=".", row.names=1)
hc = hclust(dist(t(data)))
pdf("KRAS_EGFR_BRAF.pdf", height=20, width=20)
plot(hc)
graphics.off()