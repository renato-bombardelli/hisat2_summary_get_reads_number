# hisat2_summary_get_reads_number

Python3 script to retrieve information of the number of reads aligned to a reference from a hisat2 summary file.

Usually we only need the percentage of the alignment rate, but sometimes it is usefull to have access to the number of reads aligned.

Here I gave some examples files of an hisat2 summary. and the code itself have examples extract from these files and outputs it.

The function takes two arguments: 
  file -> Hisat2 summary file to analyse and retrieve the number of reads aligned
  treatment -> (optional) the treatment itself, string
  
