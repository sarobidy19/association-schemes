#


#from sage.all import ZZ
#from sage.all import graphs
#from sage.all import SetPartitions
#from sage.all import Posets
#from sage.all import matrix
#from schemes.generic_schemes import AssociationScheme
#from schemes.schemes_with_names import base_matrix_to_adjacency_matrice


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
	"""
	Return the perfect matching association scheme with parameter equal to `self`.

	EXAMPLE:

	.. code-block:: sage

		sage: X = graphs.ShrikhandeGraph()
		sage: G = X.automorphism_group()
		sage: A = X.adjacency_matrix()
		sage: B = X.complement().adjacency_matrix()
		sage: I = matrix.identity(X.order())
		sage: AS = AssociationScheme([I,A,B])
		sage: AS1 = OrbitalSchemeTransitiveGroup(G)
		sage: AS.is_formally_self_dual()
		True
		sage: AS1.is_formally_self_dual()
		False

	"""
	n = 2*k
	V = SetPartitions(n,[2]*k)
	mat = matrix.zero(len(V))
	d = dict()
	i = 0
	for p in Posets.IntegerPartitionsDominanceOrder(n):
		if is_even_partition(p):
			d[p] = i
			i += 1
	for i in range(len(V)):
		for j in range(len(V)):
			if i >= j:
				p = cycle_type_of_perfect_matching(V[i],V[j])
				mat[i,j] = d[p]
	L = base_matrix_to_adjacency_matrices(mat+mat.transpose())
	return AssociationScheme(L)
