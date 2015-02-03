

data = read.table("GSM1536837_TCGA_20.Illumina.tumor_Rsubread_TPM_EGFRoutfile.txt", header=TRUE, sep="\t",
			 dec=".", row.names=1)
hc = hclust(dist(t(data)))
pdf("EGFR.pdf", height=20)
plot(hc)
graphics.off()