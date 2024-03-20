# wildsoybean_microbiome

Metagenomic Reads Mapping Workflow

1. Software used in this workflow
	• Perl
	• Python3
	• Bbmap
	• Samtools
	• Metabat2

2. Dataset
The metagenomic sequence data have been deposited in GenBank under the BioProject accession number PRJNA890906.

3. Mapping
nohup python bbmapbatch.py &

4. Mapped reads number (Take the sample PR300_4 as an example)
samtools view -c -f 1 -F 12 PR300_4mapped.sort.bam
