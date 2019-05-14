def get_reads_aligned(total, conc_1time, conc_more, disc_1time, new_total, disc_exactly1, disc_more, aligned_concordantly, treatment=''):
    """
	-> Retrieves the total number of reads aligned from a hisat2 summary file.
	Once the hisat2 only gives us the overall percentage, but sometimes we do need the number of reads itself.
	:param total: the first line of the hisat2 summary: "reads; of these:"
	:param conc_1time: 4th line: "aligned concordantly exactly 1 time"
	:param conc_more: 5th line: "aligned concordantly >1 times"
	:param disc_1time: 8th line: "aligned discordantly 1 time"
	:param new_total: 11th line: "mates make up the pairs; of these:"
	:param disc_exactly1: 13th line: "aligned exactly 1 time"
	:param disc_more: 14th line: "aligned >1 times"
	:param aligned_concordantly: 7th line: "pairs aligned concordantly 0 times; of these:"
	:param treatment: (Optional) Insert the treamnet #### treatment='your treatment'
	:return: 1) A print with the corresponding percentages to check in the hisat2 summary file;
		 2) The overall percentage aligned (also to check);
		 3) The NUMBER of reads aligned.
	"""

    #correct syntax to the calculation:
    #conc_exactly_1time*2 + conc_more*2 + disc_1time*2 + aligned_exactly_1time + aligned_more
    
    #concordantly aligned
    total = total
    conc_1time = conc_1time
    conc_more = conc_more

    total2 = total*2
    conc_1time2 = conc_1time*2
    conc_more2 = conc_more*2

    #aligned concordantly
    aligned_concordantly = aligned_concordantly

    #mate discordantly aligned
    new_total = new_total
    disc_1time = disc_1time
    disc_exactly1 = disc_exactly1
    disc_more = disc_more

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


print('IAC inoc rep1')
print(get_reads_aligned(2594261, 22273, 1909, 85, 5139988, 1247, 1367, 2570079))
print('IAC inoc rep2')
print(get_reads_aligned(7297868, 7321, 1720, 21, 14577612, 1101, 2137, 7288827))
print('IAC inoc rep3')
print(get_reads_aligned(8112783, 4864, 3821, 13, 16208170, 1618, 3780, 8104098))
print('SP inoc rep1')
print(get_reads_aligned(8896637, 16559, 3942, 38, 17752196, 2130, 3354, 8876136))
print('SP inoc rep2')
print(get_reads_aligned(11262410, 18665, 4223, 25, 22478994, 2352, 4078, 11239522))
print('SP inoc rep3')
print(get_reads_aligned(9747096, 29659, 6883, 70, 19420968, 3308, 4832, 9710554))
