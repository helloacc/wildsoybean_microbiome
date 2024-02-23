import os;

PR0_1=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_1_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_1_R2.fastq.gz',
      'PR0_1mapped.sam'];
PR0_2=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_2_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_2_R2.fastq.gz',
      'PR0_2mapped.sam'];
PR0_3=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_3_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_3_R2.fastq.gz',
      'PR0_3mapped.sam'];
PR0_4=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_4_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR0_4_R2.fastq.gz',
      'PR0_4mapped.sam'];  
PR100_1=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_1_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_1_R2.fastq.gz',
      'PR100_1mapped.sam'];
PR100_2=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_2_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_2_R2.fastq.gz',
      'PR100_2mapped.sam'];
PR100_3=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_3_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_3_R2.fastq.gz',
      'PR100_3mapped.sam'];
PR100_4=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_4_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR100_4_R2.fastq.gz',
      'PR100_4mapped.sam'];      
PR200_1=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_1_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_1_R2.fastq.gz',
      'PR200_1mapped.sam'];
PR200_2=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_2_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_2_R2.fastq.gz',
      'PR200_2mapped.sam'];
PR200_3=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_3_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_3_R2.fastq.gz',
      'PR200_3mapped.sam'];
PR200_4=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_4_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR200_4_R2.fastq.gz',
      'PR200_4mapped.sam']; 
PR300_1=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_1_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_1_R2.fastq.gz',
      'PR300_1mapped.sam'];
PR300_2=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_2_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_2_R2.fastq.gz',
      'PR300_2mapped.sam'];
PR300_3=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_3_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_3_R2.fastq.gz',
      'PR300_3mapped.sam'];
PR300_4=['/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_4_R1.fastq.gz',
      '/home/zhengyanfen/data/salt_stress_meta/raw_reads/PR300_4_R2.fastq.gz',
      'PR300_4mapped.sam']; 

lllll=[PR0_1,PR0_2,PR0_3,PR0_4,PR100_1,PR100_2,PR100_3,PR100_4,PR200_1,PR200_2,PR200_3,PR200_4,PR300_1,PR300_2,PR300_3,PR300_4];

scaffoldname='XN05.fna'

for i in lllll: 
    os.system('/home/zhengyanfen/miniconda3/bin/bbmap.sh in='+i[0]
              +' in2='+i[1]
              +' minid=0.95 threads=50 outm='+i[2]
              +' ref='+scaffoldname);

for file in os.listdir(os.getcwd()):
    if file.endswith('.sam'):
        outfilename = file.rstrip('.sam') + '.aln.bam'
        os.system('/home/zhengyanfen/miniconda3/bin/samtools view -bS '+file+' > '+outfilename)
for file in os.listdir(os.getcwd()):
    if file.endswith('.aln.bam'):
        outfilename = file.rstrip('.aln.bam') + '.sort.bam'
        os.system('/home/zhengyanfen/miniconda3/bin/samtools sort '+file+' -o '+outfilename + ' -@ 20')
        