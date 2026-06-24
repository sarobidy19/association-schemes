#


#from sage.all import ZZ
#from sage.all import graphs
#from sage.all import SetPartitions
#from sage.all import Posets
#from sage.all import matrix
from AssociationSchemes.generic_schemes import AssociationScheme
#from schemes.schemes_with_names import base_matrix_to_adjacency_matrice


def _is_even_partition(p):
	for x in p:
		if is_even(ZZ(x)) == False:
			return False
		else:
			pass
	return True
def _cycle_type_of_perfect_matching(P,Q):
	X = Graph()
	E = list(P) + list(Q)
	X.add_edges(E)
	cycle_type = sorted([len(x) for x in X.connected_components_subgraphs()])
	cycle_type.reverse()
	return Partition(cycle_type)

def _perfect_matching_scheme_constructor(k):
	n = 2*k
	V = SetPartitions(n,[2]*k)
	mat = matrix.zero(len(V))
	d = dict()
	i = 0
	for p in Posets.IntegerPartitionsDominanceOrder(n):
		if _is_even_partition(p):
			d[p] = i
			i += 1
	for i in range(len(V)):
		for j in range(len(V)):
			if i >= j:
				p = _cycle_type_of_perfect_matching(V[i],V[j])
				mat[i,j] = d[p]
	L = _base_matrix_to_adjacency_matrices(mat+mat.transpose())
	return L
class PerfectMatchingScheme(AssociationScheme):
	r"""
	Return the perfect matching association scheme with parameter equal to `self`.

	EXAMPLE:

	.. code-block:: python

		sage: AS = PerfectMatchingScheme(4)
		sage: AS
		A 4-class association scheme of order 105
		sage: AS.P_matrix()
		[ 1 12 12 32 48]
		[ 1  2  7 -8 -2]
		[ 1 -6  3  8 -6]
		[ 1  5 -2  4 -8]
		[ 1 -1 -2 -2  4]


	"""
	def __init__(self,k):
		self.gens = _perfect_matching_scheme_constructor(k)

	def parameter(self):
		return k

	def vertices(self):
		n = 2*k
		V = SetPartitions(n,[2]*k)
		return V
