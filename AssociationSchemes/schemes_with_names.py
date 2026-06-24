


#from permutation_group.py import PermutationGroup
#from sage.graphs.digraph import DiGraph
#from generic_schemes import AssociationScheme
#from sage.matrix.special import matrix
#from sage.rings.finite_rings.integer_mod_ring import Zmod

def OrbitalSchemeTransitiveGroup(G):

	"""
	Return the orbital scheme of the transitive group ``G``.

	INPUT:  ``G`` - a transitive group.

	OUTPUT:  orbital scheme of the transitive group ``G``.
    """
	V = G.domain()
	G = PermutationGroup(G.gens())
	S = G.orbital_digraphs()
	A = AssociationScheme([x.adjacency_matrix(vertices = V) for x in S]+[matrix.identity(len(V))])
	return A

def OrbitalSchemeGroupAction(G):

	"""
	Return the orbital scheme of the transitive group ``G``.

	INPUT:  ``G`` - a transitive group.

	OUTPUT:  orbital scheme of the transitive group ``G``.
    """

	H = G.stabilizer(G.domain()[0])
	K = G.group_action(H)
	S = sub_orbits(K)
	A = AssociationScheme([matrix.identity(K.degree())]+[x.adjacency_matrix() for x in S[0]]+[x[0].adjacency_matrix() for x in S[1]])
	return A

def JohnsonScheme(n,k):
	V = Combinations(range(1,n+1),k)
	M = zero_matrix(binomial(n,k))
	for i in range(len(V)):
		A = V[i]
		for j in range(len(V)):
			B = V[j]
			M[i,j] = k-len(set(A).intersection(set(B)))
	return AssociationScheme(base_matrix_to_adjacency_matrices(M))

def GrassmannScheme(q,n,k):
	m = min(n-k,k)
	X = graphs.GrassmannGraph(q,n,m)
	V = X.vertices()
	M = zero_matrix(X.order())
	for i in range(len(V)):
		A = V[i]
		for j in range(len(V)):
			B = V[j]
			M[i,j] = m-len(A.intersection(B))
	return AssociationScheme(base_matrix_to_adjacency_matrices(M))

def HammingScheme(D,q):
	V = Tuples(range(1,q+1),D)
	M = zero_matrix(len(V))
	for i in range(len(V)):
		for j in range(len(V)):
			test = lambda k: V[i][k] == V[j][k]
			M[i,j] = D - len(list(filter(test,range(D))))
	L = base_matrix_to_adjacency_matrices(M)
	return AssociationScheme(L)


def GroupScheme(G):
	group_ordering = [G[i] for i in range(G.order())]
	n = G.order()
	CC = G.conjugacy_classes_representatives()
	M = []
	for i in range(len(CC)):
		rows = []
		for g in group_ordering:
			row = []
			for h in group_ordering:
				if h*g.inverse() in G.conjugacy_class(CC[i]):
					row.append(1)
				else:
					row.append(0)
			rows.append(row)
		M.append(Matrix(rows))
	A = AssociationScheme(M)
	return A

def LeeScheme(q,k):
	# combinatorial objects
	G = Zmod(q)
	V = Tuples(G,k)
	M = zero_matrix(len(V))
	s = floor(q/2)
	# dictionary for lee compositions
	d = dict()
	lee_compositions = IntegerVectors(k,s+1).list()
	for i in range(len(lee_compositions)):
		d[i] = lee_compositions[i]
	# definition of the base matrix
	for i in range(len(V)):
		x = V[i]
		for j in range(len(V)):
			y = V[j]
			z = [G(x[i]-y[i]) for i in range(k)]
			lc = []
			for u in range(s+1):
				c = 0
				for v in range(len(z)):
					if z[v] == G(u) or z[v] == G(-u):
						c += 1
				lc.append(c)
			#lc,z
			for u in d.keys():
				if tuple(d[u]) == tuple(lc):
					#d[u], lc, u, i,j
					M[i,j] = u
	L = base_matrix_to_adjacency_matrices(M)
	return AssociationScheme(L)





"""def GrassmannScheme(q,n,k):
	V = VectorSpace(GF(q),n)
	D = list(V.subspaces(k))
	M = zero_matrix(len(D))
	for i in [0..len(D)-1]:
		A = D[i]
		for j in [0..len(D)-1]:
			B = D[j]
			M[i,j] = k-(A.intersection(B)).dimension()
	return AssociationScheme(base_matrix_to_adjacency_matrices(M))"""
