def read_reads(fname):
	""" Read short reads in FASTA format. It is assumed that one line in the input file correspond to one read. """
	f = open(fname, 'r')
	lines = f.readlines()
	f.close()
	reads = []

	for line in lines:
		if line[0] != '>':
			reads = reads + [line.rstrip()]

	return reads

def construct_graph(reads):
	return 0

def output_contigs(g):
	return 0


# Main script
fname = 'g200reads.fa'
reads = read_reads(fname)
print reads
# g = construct_graph(reads)
# contig = output_contigs(g)
