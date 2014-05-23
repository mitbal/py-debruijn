class Node:
    def __init__(self, lab):
        self.label = lab
        self.indegree = 0
        self.outdegree = 0

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
    edges = dict()
    vertices = dict()

    for read in reads:
        i = 0
        while i+k < len(read):
            v1 = read[i:i+k]
            v2 = read[i+1:i+k+1]
            if v1 in edges.keys():
                vertices[v1].outdegree += 1
                edges[v1] += [Edge(v2)]
            else:
                vertices[v1] = Node(v1)
                vertices[v1].outdegree += 1
                edges[v1] = [Edge(v2)]
            if v2 in edges.keys():
                vertices[v2].indegree += 1
            else:
                vertices[v2] = Node(v2)
                vertices[v2].indegree += 1
                edges[v2] = []
            i += 1

    return (vertices, edges)

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

def print_graph(g):
    V = g[0]
    E = g[1]
    for k in V.keys():
        print "name: ", V[k].label, ". indegree: ", V[k].indegree, ". outdegree: ", V[k].outdegree
        print "Edges: "
        for e in E[k]:
            print e.label

# Main script
fname = 'g200reads.fa'
reads = read_reads(fname)
# print reads

test = ['bcdefg', 'defghi', 'abcd']
g = construct_graph(test, 3)
print_graph(g)
# for k in g.keys():
#   print k, g[k]
# g = construct_graph(reads)
# contig = output_contigs(g)
# print contig