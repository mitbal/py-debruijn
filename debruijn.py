class Node:
	def __init__(self, lab):
		self.label = lab
		self.edge = []

class Edge:
	def __init__(self, lab):
		self.label = lab

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

def construct_graph(reads, k):
	""" Construct de bruijn graph from sets of short reads with k length word"""
	nodes = dict()

	for read in reads:
		i = 0
		while i+k < len(read):
			v1 = read[i:i+k]
			v2 = read[i+1:i+k+1]
			if v1 in nodes.keys():
				nodes[v1] += [Edge(v2)]
			else:
				nodes[v1] = [Edge(v2)]
			if v2 not in nodes.keys():
				nodes[v2] = []
			i += 1

	return nodes


def output_contigs(g):
	""" Perform searching for Eulerian path in the graph to output genome assembly"""

	# Pick starting node (for now, at random)
	start = g.keys()[0]

	contig = start
	current = start
	while len(g[current]) > 0:
		# Pick the next node to be traversed (for now, at random)
		next = g[current][0]
		del g[current][0]
		contig += next.label[-1]
		current = next.label

	return contig

# Main script
fname = 'g200reads.fa'
reads = read_reads(fname)
# print reads

test = ['bcdefg', 'defghi', 'abcd']
g = construct_graph(test, 3)
# for k in g.keys():
# 	print k, g[k]
# g = construct_graph(reads)
contig = output_contigs(g)
print contig