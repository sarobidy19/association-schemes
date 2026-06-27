#

from sage.all import ComplexField
from sage.all import RationalField
from sage.graphs.digraph import DiGraph
from sage.graphs.graph import Graph
#from sage.matrix.special import matrix, Matrix
from sage.matrix.matrix_space import MatrixSpace

CC = ComplexField()
QQ = RationalField()


class AssociationScheme:
	r"""
		AssociationScheme(adjacency_matrices)
		INPUT:
		 - adjacency_matrices: a list of 01-matrices forming an association scheme.
		OUTPUT:
		  A class called AssociationScheme.


		**Example:** The Johnson scheme J(5,2) can be obtained as follows.

		.. code-block:: sage

			sage: X = graphs.PetersenGraph()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])

	"""
	def __init__(self,gens):
		self.gens = gens

	def __repr__(self):
		return "A {0}-class association scheme of order {1}".format(len(self.gens)-1,self.gens[0].dimensions()[0])

	def order(self):
		r"""Return the number of vertices in self.

		.. code-block:: sage

				sage: X = graphs.PetersenGraph()
				sage: A = X.adjacency_matrix()
				sage: B = X.complement().adjacency_matrix()
				sage: I = matrix.identity(X.order())
				sage: AS = AssociationScheme([I,A,B])
				sage: AS.order()
				10

		"""
		return self.gens[0].dimensions()[0]
	def rank(self):
		r"""Return the number of relations in self.

		.. code-block:: sage

				sage: X = graphs.PetersenGraph()
				sage: A = X.adjacency_matrix()
				sage: B = X.complement().adjacency_matrix()
				sage: I = matrix.identity(X.order())
				sage: AS = AssociationScheme([I,A,B])
				sage: AS.rank()
				3
		"""
		return len(self.gens)
	def adjacency_matrices(self):
		r"""Return the adjacency matrices of self as a list.

		.. code-block:: sage

			sage: X = graphs.PetersenGraph()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.adjacency_matrices()
			[
			[1 0 0 0 0 0 0 0 0 0]  [0 1 0 0 1 1 0 0 0 0]  [0 0 1 1 0 0 1 1 1 1]
			[0 1 0 0 0 0 0 0 0 0]  [1 0 1 0 0 0 1 0 0 0]  [0 0 0 1 1 1 0 1 1 1]
			[0 0 1 0 0 0 0 0 0 0]  [0 1 0 1 0 0 0 1 0 0]  [1 0 0 0 1 1 1 0 1 1]
			[0 0 0 1 0 0 0 0 0 0]  [0 0 1 0 1 0 0 0 1 0]  [1 1 0 0 0 1 1 1 0 1]
			[0 0 0 0 1 0 0 0 0 0]  [1 0 0 1 0 0 0 0 0 1]  [0 1 1 0 0 1 1 1 1 0]
			[0 0 0 0 0 1 0 0 0 0]  [1 0 0 0 0 0 0 1 1 0]  [0 1 1 1 1 0 1 0 0 1]
			[0 0 0 0 0 0 1 0 0 0]  [0 1 0 0 0 0 0 0 1 1]  [1 0 1 1 1 1 0 1 0 0]
			[0 0 0 0 0 0 0 1 0 0]  [0 0 1 0 0 1 0 0 0 1]  [1 1 0 1 1 0 1 0 1 0]
			[0 0 0 0 0 0 0 0 1 0]  [0 0 0 1 0 1 1 0 0 0]  [1 1 1 0 1 0 0 1 0 1]
			[0 0 0 0 0 0 0 0 0 1], [0 0 0 0 1 0 1 1 0 0], [1 1 1 1 0 1 0 0 1 0]
			]

		"""
		L = self.gens
		n = self.order()
		for A in L:
			if A == sage.all.identity_matrix(n):
				j = L.index(A)
		adjacency_matrices = [L[j]]
		for i in range(len(L)):
			if i != j:
				adjacency_matrices.append(L[i])
		return adjacency_matrices
	def base_matrix(self):
		r"""

		Return the base matrix of self. If :math:`(\Omega,\mathcal{R})` is an association scheme with adjacency matrices :math:`A_0 = I, A_1,\ldots, A_d`, then the *base matrix* of :math:`(\Omega,\mathcal{R})` is the matrix
		:math:`0A_0 + 1A_1+2A_2+ \ldots+ dA_d`.

		.. code-block:: sage

			sage: X = graphs.PetersenGraph()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.base_matrix()
			[0 1 2 2 1 1 2 2 2 2]
			[1 0 1 2 2 2 1 2 2 2]
			[2 1 0 1 2 2 2 1 2 2]
			[2 2 1 0 1 2 2 2 1 2]
			[1 2 2 1 0 2 2 2 2 1]
			[1 2 2 2 2 0 2 1 1 2]
			[2 1 2 2 2 2 0 2 1 1]
			[2 2 1 2 2 1 2 0 2 1]
			[2 2 2 1 2 1 1 2 0 2]
			[2 2 2 2 1 2 1 1 2 0]
		"""
		L = self.adjacency_matrices()
		A = 0*L[0]
		r = self.rank()
		for i in range(1,r):
			A += i*L[i]
		return A
	def intersection_number(self,i,j,k):
		r"""
		Return the intersection number :math:`p_{ij}^k` of the association scheme ``self``.


		INPUT: integers :math:`i,j,` and :math:`k` between :math:`0` and the :math:`r`, where :math:`r+1` is the rank of the association scheme.

		OUTPUT: the value of :math:`p_{ij}^k`.

		EXAMPLE:

		For example, the intersection numbers of the affine polar graph :math:`VO_6^-(2)` can be computed as follows.

		.. code-block:: sage

		        sage: X = graphs.AffineOrthogonalPolarGraph(6,2,sign="-")
		        sage: A = X.adjacency_matrix()
		        sage: B = X.complement().adjacency_matrix()
		        sage: I = matrix.identity(X.order())
		        sage: AS = AssociationScheme([I,A,B])
		        sage: AS.intersection_number(0,1,1)
		        1
		        sage: AS.intersection_number(1,1,1)
		        10
		        sage: AS.intersection_number(2,2,1)
		        20
		        sage: AS.intersection_number(2,2,2)
		        20
		"""
		n = self.order()
		M = self.base_matrix()
		u = list(M[0]).index(k)
		check = lambda l: M[0,l] == i and M[l,u] == j
		return len(list(filter(check,range(n))))
	def is_commutative(self):

		r"""
	    Return whether or not ``self`` is a commutative association scheme.

	    The :math:`d`-class assocition scheme :math:`(\Omega,\mathcal{R})` is commutative if its intersection numbers satisfy :math:`p_{ij}^k = p_{ji}^k`, for all :math:`0\leq i,j,k\leq d`.

	    EXAMPLE:

	    .. code-block:: sage

		    sage: AS = OrbitalSchemeTransitiveGroup(group_acting_on_subsets(PSL(2,7),2))
		    sage: AS.is_commutative()
		    False
		    sage: AS = OrbitalSchemeTransitiveGroup(group_acting_on_subsets(AlternatingGroup(7),2))
		    sage: AS.is_commutative()
		    True

	    """
		key = True
		r = self.rank()
		for i in range(r):
			for j in range(r):
				for k in range(r):
					if i != j and self.intersection_number(i,j,k) != self.intersection_number(j,i,k):
						return False
					else:
						pass
		return True
	def automorphism_group(self):

		r"""
		Return the automorphism group of ``self``, that is, the permutation group that preserves all relations of ``self``.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: K = AS.automorphism_group()
			sage: K.structure_description()
			'(((C4 x C4) : C3) : C2) : C2'
			sage: K.is_transitive()
			True
		"""
		L = self.adjacency_matrices()
		r = self.rank()
		G = DiGraph(L[1]).automorphism_group()
		for i in range(2,r):
			G = G.intersection(DiGraph(L[i]).automorphism_group())
		return G
	def is_schurian(self):

		r"""
		Return whether or not ``self`` is Schurian, that is, its relations are the orbitals of a transitive group

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: AS1 = OrbitalSchemeTransitiveGroup(G)
			sage: AS1.is_schurian()
			True
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS2 = AssociationScheme([I,A,B])
			sage: AS2.is_schurian()
			False
		"""
		G = self.automorphism_group()
		S = G.stabilizer(G.domain()[0])
		return len(S.orbits()) == self.rank()
	def character_table(self):

		r"""
		Return the first eigenmatrix of ``self``.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.character_table()
			[ 1  6  9]
			[ 1  2 -3]
			[ 1 -2  1]
			sage: AS1 = OrbitalSchemeTransitiveGroup(G)
			sage: AS1.character_table()
			[ 1  6  6  3]
			[ 1  2 -2 -1]
			[ 1 -2 -2  3]
			[ 1 -2  2 -1]
		"""

		if self.is_commutative() == False:
			return "Association Scheme not commutative"
		else:
			table = []
			T = _common_eigenvectors(self.adjacency_matrices()) #can contain a matrix of zero
			r = self.rank()
			for i in range(r):
				row = []
				for j in range(r):
						row.append(T[i][0][j])
				table.append(row)
			return Matrix(table)

	def P_matrix(self):

		r"""Return the first eigenmatrix of ``self``. This is the same as `character_table()`."""

		if self.is_commutative() == False:
			return "Error: Association Scheme not commutative"
		else:
			return self.character_table()
	def Q_matrix(self):

		r"""Return the first eigenmatrix of ``self``.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.Q_matrix()
			[ 1  6  9]
			[ 1  2 -3]
			[ 1 -2  1]
			sage: AS1 = OrbitalSchemeTransitiveGroup(G)
			sage: AS1.Q_matrix()
			[ 1  6  3  6]
			[ 1  2 -1 -2]
			[ 1 -2 -1  2]
			[ 1 -2  3 -2]

		"""
		if self.is_commutative() == False:
			return "Error: Association Scheme not commutative"
		else:
			P = self.character_table()
			return self.order()*P.inverse()
	def dimension_of_t_zero(self,matrix=False):

		r"""
		Return the dimension of the subspace :math:`T_0` of the Terwilliger algebra with respect to any vertex.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: AS = OrbitalSchemeTransitiveGroup(G)
			sage: AS.dimension_of_t_zero()
			31
			sage: AS.dimension_of_t_zero(matrix=True)
			[1 1 1 1]
			[1 4 3 2]
			[1 3 4 2]
			[1 2 2 2]

		"""
		if matrix == False:
			d = 0
			r = self.rank()
			T = Tuples(range(r),3)
			for x in T:
				i,j,k = x
				if self.intersection_number(i,j,k) != 0:
					d += 1
			return d
		elif matrix == True:
			r = self.rank()
			mat = zero_matrix(r)
			T = Tuples(range(r),2)
			for x in T:
				i,k = x
				check = lambda j: self.intersection_number(i,j,k)  != 0
				mat[i,k] = len(list(filter(check,range(r))))
			return mat

	def dimension_of_centralizer_algebra(self,v,matrix = False):

		r"""

		Return the dimension of the centralizer algebra of the stabilizer of `vertex` in the automorphism group of ``self`` if ``matrix=False``. If ``matrix=True``, then it returns the block dimension decomposition of the centralizer algebra.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: AS = OrbitalSchemeTransitiveGroup(G)
			sage: AS.dimension_of_t_zero()
			sage: AS.dimension_of_centralizer_algebra(1)
			31
			sage: AS.dimension_of_centralizer_algebra(1,matrix=True)
			[1 1 1 1]
			[1 4 2 3]
			[1 2 2 2]
			[1 3 2 4]

		"""
		if matrix == False:
			G = self.automorphism_group()
			S = G.stabilizer(v)
			d = 0
			for x in S.orbits():
				K = S.stabilizer(x[0])
				d += len(K.orbits())
			return d
		elif matrix == True:
			G = self.automorphism_group()
			S = G.stabilizer(G.domain()[0])
			L = list(S.orbits())
			mat = []
			for x in L:
				K = S.stabilizer(x[0])
				T = [0]*len(L)
				for y in K.orbits():
					for Z in L:
						if y[0] in Z:
							j = L.index(Z)
							T[j] = T[j] + 1
						else:
							pass
				mat.append(T)
			return Matrix(mat)

	def ratio_bound(self,i):

		r"""
		Return the value of Hoffman's ratio bound for the i-th graph, if it is symmetric.

		EXAMPLE:

		.. code-block:: sage

			sage: AS = JohnsonScheme(8,3)
			sage: AS.ratio_bound(0)
			'... the index needs to be larger than 0'
			sage: AS.ratio_bound(1)
			28/3
			sage: AS.ratio_bound(2)
			8
			sage: AS.ratio_bound(3)
			21
		"""
		A = self.adjacency_matrices()[i]
		if A == matrix.identity(self.order()):
			return "... the index needs to be larger than 0"
		else:
			if A.is_symmetric() == False:
				return "... the corresponding relation is not symmetric"
			else:
				X = Graph(A)
				Ev = set(X.spectrum())
				return X.order()/(1-max(Ev)/min(Ev))
	def TerwilligerAlgebra(self,v,ring = CC):

		r"""
		Return the Terwilliger algebra, over `ring`, of `self` with respect to `vertex`.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: AS = OrbitalSchemeTransitiveGroup(G)
			sage: T = AS.TerwilligerAlgebra(1,ring=CC)
			sage: T
			Free module generated by {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30} over Complex Field with 53 bits of precision
			sage: T.dimension()
			31

		"""
		L = self.adjacency_matrices()
		D = [matrix.diagonal(A[v]) for A in L]
		gens = L + D
		n = self.order()
		M = MatrixSpace(ring, n, n)
		T = M.subalgebra(gens)
		return T
	def graphs_in_scheme(self,digraphs=False):

		r"""

		Return the graphs corresponding to symmetric classes of ``self`` if ``digraphs = False``, otherwise, all digraphs of the association scheme.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: AS = OrbitalSchemeTransitiveGroup(G)
			sage: AS.graphs_in_scheme()
			[Graph on 16 vertices, Graph on 16 vertices, Graph on 16 vertices]

		"""
		L = self.adjacency_matrices()
		if digraphs == False:
			grphs = []
			for A in L:
				if A != matrix.identity(self.order()):
					if A.is_symmetric():
						grphs.append(Graph(A,vertex_labels=range(1,1+A.dimensions()[0])))
			return grphs
		else:
			grphs = []
			for A in L:
				if A != matrix.identity(self.order()) and A.is_symmetric():
					grphs.append(Graph(A,vertex_labels=range(1,1+A.dimensions()[0])))
				if  A != matrix.identity(self.order()) and A.is_symmetric() == False:
					grphs.append(DiGraph(A,vertex_labels=range(1,1+A.dimensions()[0])))
			return grphs
	def is_formally_self_dual(self):

		r"""
		Return whether `self` is formally self dual. That is, whether $Q = \overline{P}$.

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
		return self.P_matrix() == self.Q_matrix().conjugate_transpose().transpose()
	def krein_parameters(self,i,j,k):

		r"""
		Return the value of the Krein parameter :math:`q_{ij}^k`.

		INPUT: integers :math:`i,j,` and :math:`k` between :math:`0` and the :math:`r`, where :math:`r+1` is the rank of the association scheme.

		OUTPUT: the value of :math:`q_{ij}^k`.

		EXAMPLE:

		.. code-block:: sage

			sage: AS = HammingScheme(5,2)
			sage: AS.krein_parameters(1,1,1)
			0
			sage: AS.krein_parameters(2,2,2)
			0
			sage: AS.krein_parameters(2,2,1)
			0
			sage: AS.krein_parameters(2,2,0)
			5
		"""

		T = _common_eigenvectors(self.adjacency_matrices())
		return self.order()*(T[k][1]*(_Schur_multiplication(T[i][1],T[j][1],ring))).trace()/(T[k][1]).trace()

	def adjacency_algebra(self,ring):

		r"""
		Return the adjacency algebra of `self` over the commutative ring ``ring``. That is, the algebra generated by the adjacency matrices, over the commutative algebra ``ring``.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.adjacency_algebra(ring=CC)
			Free module generated by {0, 1, 2} over Complex Field with 53 bits of precision
			sage: AS.adjacency_algebra(ring=ZZ)
			Free module generated by {0, 1, 2} over Integer Ring
			sage: AS.adjacency_algebra(ring=QQ)
			Free module generated by {0, 1, 2} over Rational Field

		"""
		L = self.adjacency_matrices()
		n = self.order()
		M = MatrixSpace(ring, n, n)
		B = M.subalgebra(L)
		return B
	def bose_mesner_algebra(self):
		"""Return the Bose-Mesner algebra of the association scheme. See also adjacency_algebra()."""
		return self.adjacency_algebra(CC)
	#def is_coherent_configuration(self):
	def is_triply_regular(self):

		r"""
		Return whether or not the association scheme is triply regular.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.HigmanSimsGraph()
			sage: A = X.adjacency_matrix()
			sage: B = X.complement().adjacency_matrix()
			sage: I = matrix.identity(X.order())
			sage: AS = AssociationScheme([I,A,B])
			sage: AS.is_triply_regular()
			True


		"""
		return self.TerwilligerAlgebra(1).dimension() == self.dimension_of_t_zero()

	def is_AssociationScheme(self):
		r"""
		Return whether ``self`` is an association scheme.

		EXAMPLE:

		.. code-block:: sage

			sage: AS = JohnsonScheme(7,3)
			sage: I,A,B,C = AS.adjacency_matrices()
			sage: AS1 = AssociationScheme([I,A+B+C])
			sage: AS1.is_AssociationScheme()
			True
			sage: AS2 = AssociationScheme([I,A+B])
			sage: AS2.is_AssociationScheme()
			False
			sage: AS3 = AssociationScheme([I,A+B,C])
			sage: AS3.is_AssociationScheme()
			False



		"""
		L = self.adjacency_matrices()
		r = len(L)
		if sum(L) != matrix.ones(self.order()):
			#print ("matrices not summing to the all-ones matrix ...")
			return False
		else:
			for i in range(r):
				if L[i].transpose() in L:
					pass
				else:
					#print ("matrices not closed under transposition ...")
					return False
			for i in range(r):
				for j in range(r):
					A = L[i]*L[j]
					B = zero_matrix(self.order())
					for k in range(r):
						B += self.intersection_number(i,j,k)*L[k]
					if A == B:
						pass
					else:
						#print ("product of certain matrices not in the algebra ...")
						return False
		return True
	def fusion(self,P,return_scheme = False):
		r"""
		Return whether the partition ``P`` of the vertices is an association scheme.

		EXAMPLE:

		.. code-block:: sage

			sage: X = graphs.ShrikhandeGraph()
			sage: G = X.automorphism_group()
			sage: G = PermutationGroup(G.gens())
			sage: AS = OrbitalSchemeTransitiveGroup(G)
			sage: L = AS.adjacency_matrices()
			sage: L[3]
			[1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
			[0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
			[0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0]
			[0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0]
			[0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0]
			[0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0]
			[0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
			[0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
			[0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
			[0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]
			[0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0]
			[0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0]
			[0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0]
			[0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
			[0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
			[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]
			sage: AS.fusion([[0],[1,2,3]])
			False
			sage: AS.fusion([[3],[0,1,2]])
			True
			sage: AS.fusion([[3],[0,1,2]],return_scheme=True)
			(True, <__main__.AssociationScheme object at 0x720021e86890>)
			sage: AS.fusion([[3],[0,1],[2]],return_scheme=True)
			(True, <__main__.AssociationScheme object at 0x720022477e70>)
		"""
		V = []
		L = self.adjacency_matrices()
		for x in P:
			B = sum([L[i] for i in x])
			V.append(B)
		AS = AssociationScheme(V)
		if AS.is_AssociationScheme() == False:
			return False
		elif AS.is_AssociationScheme() == True:
			if return_scheme == False:
				return True
			elif return_scheme == True:
				return True,AS

	def inner_distribution(self,Y):
		v = []
		V = range(self.order())
		for i in V:
			if i in Y:
				v.append(1)
			else:
				v.append(0)
		v = Matrix(v)
		L = self.adjacency_matrices()
		inner_dist = [(1/len(Y)*v*L[i]*v.transpose())[0,0] for i in range(self.rank())]
		return Matrix(QQ,inner_dist)

def _common_eigenvectors(L):
	eigenspaces_blocks = _spectral_decomposition_of_matrix(L[0])
	for i in range(1,len(L)):
		A = L[i]
		new_eigenspaces_blocks = []
		for (x,P) in eigenspaces_blocks:
			B = P.conjugate_transpose()*A*P
			if B.rank() == 1:
				for ev in set(B.eigenvalues()):
					if ev != 0:
						break
				new_eigenspaces_blocks.append((x+[ev],P))
			else:
				Ev = _spectral_decomposition_of_matrix(B)
				if len(Ev) == 1:
					y,C = Ev[0]
					new_eigenspaces_blocks.append((x+y,P*C))
				else:
					for (y,C) in Ev:
						if y[0] != 0:
							new_eigenspaces_blocks.append((x+y,P*C))
						elif y[0] == 0 and A == B:
							new_eigenspaces_blocks.append((x+y,P*C))
		eigenspaces_blocks = new_eigenspaces_blocks
		common_eigenspaces = []
		for T in eigenspaces_blocks:
			if T[1] == zero_matrix(A.dimensions()[0]):
				pass
			else:
				common_eigenspaces.append(T)
	return common_eigenspaces


def _spectral_decomposition_of_matrix(A):
	E = A.right_eigenspaces()
	eigenvalues = [E[i][0] for i in range(len(E))]
	mats = [E[i][1].matrix() for i in range(len(E))]
	orthogonal_mats = [x.gram_schmidt()[0] for x in mats]
	spectral_eigenspaces = []
	for i in range(len(orthogonal_mats)):
		x = orthogonal_mats[i]
		r = x.rows()
		B = zero_matrix(A.dimensions()[0])
		for a in r:
			a = Matrix(a)
			B += a.transpose()*a/(a*a.conjugate_transpose()).list()[0]
		spectral_eigenspaces.append(([E[i][0]],B))
	return spectral_eigenspaces

def _Schur_multiplication(A,B,ring = QQ):
	C = zero_matrix(ring,A.dimensions()[0])
	for i in range(A.dimensions()[0]):
		for j in range(A.dimensions()[0]):
			C[i,j] = A[i,j]*B[i,j]
	return C


#def

def _base_matrix_to_adjacency_matrices(M):
	d = len(set(M[0]))
	adjacency_matrices = []
	for i in range(d):
		A = zero_matrix(M.dimensions()[0])
		T = Tuples(range(M.dimensions()[0]),2)
		for x in T:
			s,t = x
			if M[s,t] == i:
				A[s,t] = 1
		adjacency_matrices.append(A)
	return adjacency_matrices
