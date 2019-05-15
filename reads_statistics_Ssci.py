def get_reads_aligned(file, treatment=''):
    """
	-> Retrieves the total number of reads aligned from a hisat2 summary file.
	Once the hisat2 only gives us the overall percentage, but sometimes we do need the number of reads itself.
	:param file: Hisat2 summary file
	:param treatment: (Optional) Insert the treamnet #### treatment='your treatment'
	:return: 1) A print with the corresponding percentages to check in the hisat2 summary file;
		 2) The overall percentage aligned (also to check);
		 3) The NUMBER of reads aligned.
	"""

    #correct syntax to the calculation:
    #conc_exactly_1time*2 + conc_more*2 + disc_1time*2 + aligned_exactly_1time + aligned_more
    
    complete_summary = []
    with open(file) as summary:
            for line in summary:
                line = line.split()
                complete_summary.append(line[0])

    #concordantly aligned
    total = int(complete_summary[0])
    conc_1time = int(complete_summary[3])
    conc_more = int(complete_summary[4])

    total2 = total*2
    conc_1time2 = conc_1time*2
    conc_more2 = conc_more*2

    #aligned concordantly
    aligned_concordantly = int(complete_summary[6])

    #mate discordantly aligned
    new_total = int(complete_summary[10])
    disc_1time = int(complete_summary[7])
    disc_exactly1 = int(complete_summary[12])
    disc_more = int(complete_summary[13])

    #just to print the treatment
    if treatment not in '':
        print(f'Analasing - {treatment}')

    #output of the function
    print(f'''
    %conc_1time -> {(conc_1time2*100)/total2:.2f}
    %conc_>1 -> {(conc_more2*100)/total2:.2f}
    %disc_1time -> {(disc_1time*100)/aligned_concordantly:.2f}
    %disc_exact_1time -> {(disc_exactly1*100)/new_total:.2f}
    %disc_>1 -> {(disc_more*100)/new_total:.2f}
    ''')

    sum_aligned_reads = conc_1time2 + conc_more2 + disc_1time * 2 + disc_exactly1 + disc_more
    perc = (sum_aligned_reads*100)/total2
    print(f'Overall alignment rate: {perc:.8f}%')

    reads_aligned = sum_aligned_reads
    return(f'The number of aligned reads is: {reads_aligned}')



print(get_reads_aligned('summary_align_IACinoc_rep1_cutadapt.txt', treatment='IACinoc_rep1'))

print(get_reads_aligned('summary_align_IACinoc_rep2_cutadapt.txt', treatment='IACinoc_rep2'))

print(get_reads_aligned('summary_align_IACinoc_rep3_cutadapt.txt', treatment='IACinoc_rep3'))
