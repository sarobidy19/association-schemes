def is_even_partition(p):
	for x in p:
		if is_even(ZZ(x)) == False:
			return False
		else:
			pass
	return True
def cycle_type_of_perfect_matching(P,Q):
	X = Graph()
	E = list(P) + list(Q)
	X.add_edges(E)
	cycle_type = sorted([len(x) for x in X.connected_components_subgraphs()])
	cycle_type.reverse()
	return Partition(cycle_type)
def PerfectMatchingScheme(k):
	n = 2*k
	V = SetPartitions(n,[2]*k)
	mat = zero_matrix(len(V))
	d = dict()
	i = 0
	for p in Posets.IntegerPartitionsDominanceOrder(n):
		if is_even_partition(p):
			d[p] = i
			i += 1 
	for i in [0..len(V)-1]:
		for j in [i..len(V)-1]:
			p = cycle_type_of_perfect_matching(V[i],V[j])
			mat[i,j] = d[p]
	L = base_matrix_to_adjacency_matrices(mat+mat.transpose())
	return association_scheme(L) 
