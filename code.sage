class association_scheme:
	def __init__(self,gens):
		self.gens = gens 
	def order(self):
		return self.gens[0].dimensions()[0]
	def rank(self):
		return len(self.gens)
	def adjacency_matrices(self):
		return self.gens
	def base_matrix(self):
		L = self.adjacency_matrices()
		A = 0*L[0]
		r = self.rank()
		for i in [1..r-1]:
			A += i*L[i]
		return A
	def intersection_number(self,i,j,k):
		n = self.order()
		M = self.base_matrix()
		u = list(M[0]).index(k)
		check = lambda l: M[0,l] == i and M[l,u] == j
		return len(list(filter(check,[0..n-1])))
	def is_commutative(self):
		key = True
		r = self.rank()
		for i in [0..r-1]:
			for j in [0..r-1]:
				for k in [0..r-1]:
					if i != j and self.intersection_number(i,j,k) != self.intersection_number(j,i,k):
						return False
					else:
						pass
		return True
	def automorphism_group(self):
		L = self.adjacency_matrices()
		r = self.rank()
		G = DiGraph(L[1]).automorphism_group()
		for i in [2..r-1]:
			G = G.intersection(DiGraph(L[i]).automorphism_group())
		return G
	def is_schurian(self):
		G = self.automorphism_group()
		S = G.stabilizer(G.domain()[0])
		return len(S.orbits()) == self.rank()
	def class_with_maximum_number_of_eigenvalues(self):
		L = self.adjacency_matrices()
		m = 1
		y = L[0]
		for x in L:
			t = len(set(x.eigenvalues()))
			if t > m:
				m = t
				y = x
		return m,y
	def spectral_decomposition(self):
		m,y = self.class_with_maximum_number_of_eigenvalues()
		X = Graph(y)
		n = X.order()
		E = X.eigenspaces()
		eigenvalues = [x[0] for x in E]
		mats = [x[1].matrix() for x in E]
		orthogonal_mats = [x.gram_schmidt()[0] for x in mats]
		idempotents = []
		for x in orthogonal_mats:
			r = x.rows()
			A = zero_matrix(n,n)
			for a in r:
				a = Matrix(a)
				A += a.transpose()*a/(a*a.transpose()).list()[0]
			idempotents.append(A)
		return eigenvalues,idempotents
	def character_table(self):
		if self.is_commutative() == False:
			return "Error: Association Scheme not commutative"
		else:
			table = []
			T = common_eigenvectors(self.adjacency_matrices())
			r = self.rank()
			for i in [0..r-1]:
				row = []
				for j in [0..r-1]:
					row.append(T[i][0][j])
				table.append(row)
			return Matrix(table)

	def P_matrix(self):
		if self.is_commutative() == False:
			return "Error: Association Scheme not commutative"
		else:
			return self.character_table()
	def Q_matrix(self):
		if self.is_commutative() == False:
			return "Error: Association Scheme not commutative"
		else:
			P = self.character_table()
			return self.order()*P.inverse()
	def dimension_of_t_zero(self):
		d = 0
		r = self.rank()
		T = Tuples([0..r-1],3)
		for x in T:
			i,j,k = x
			if self.intersection_number(i,j,k) != 0:
				d += 1
		return d
	def dimension_of_centralizer_algebra(self,v):
		G = self.automorphism_group()
		S = G.stabilizer(v)
		d = 0
		for x in S.orbits():
			K = S.stabilizer(x[0])
			d += len(K.orbits())
		return d
	def ratio_bound(self,i):
		A = self.adjacency_matrices()[i]
		if A == matrix.identity(self.order()):
			return "... the index needs to be larger than 0"
		else:
			if A.is_symmetric() == False:
				return "... the corresponding relation is not symmtric"
			else:
				X = Graph(A)
				Ev = set(X.spectrum())
				return X.order()/(1-max(Ev)/min(Ev))
	def TerwilligerAlgebra(self,v):
		L = self.adjacency_matrices()
		D = [diagonal_matrix(A[v]) for A in L]
		gens = L + D
		n = self.order()
		M = MatrixSpace(QQ, n, n)
		T = M.subalgebra(gens)
		return T
	def graphs_in_scheme(self):
		L = self.adjacency_matrices()
		grphs = []
		for A in L:
			if A != matrix.identity(self.order()):
				if A.is_symmetric():
					grphs.append(Graph(A))
		return grphs
	def is_formally_self_dual(self):
		return self.P_matrix() == self.Q_matrix().conjugate_transpose().transpose()





def conjugacy_class_scheme(G):
	group_ordering = [G[i] for i in [0..G.order()-1]]
	n = G.order()
	CC = G.conjugacy_classes_representatives()
	M = []
	for i in [0..len(CC)-1]:
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
	A = association_scheme(M)
	return A

def load_all_functions():
	load("https://raw.githubusercontent.com/sarobidy19/Intersection-density-sage/refs/heads/main/all-functions.sage")
load_all_functions()

def OrbitalSchemeTransitiveGroup(G):
	S = sub_orbits(G)
	A = association_scheme([matrix.identity(G.degree())]+[x.adjacency_matrix() for x in S[0]]+[x[0].adjacency_matrix() for x in S[1]])
	return A

def OrbitalSchemeGroupAction(G):
	H = G.stabilizer(G.domain()[0])
	K = group_action_on_cosets(G,H)
	S = sub_orbits(K)
	A = association_scheme([matrix.identity(K.degree())]+[x.adjacency_matrix() for x in S[0]]+[x[0].adjacency_matrix() for x in S[1]])
	return A

def base_matrix_to_adjacency_matrices(M):
	d = len(set(M[0]))
	adjacency_matrices = []
	for i in [0..d-1]:
		A = zero_matrix(M.dimensions()[0])
		T = Tuples([0..M.dimensions()[0]-1],2)
		for x in T:
			s,t = x
			if M[s,t] == i:
				A[s,t] = 1
		adjacency_matrices.append(A)
	return adjacency_matrices

def JohnsonScheme(n,k):
	V = Combinations([1..n],k)
	M = zero_matrix(binomial(n,k))
	for i in [0..len(V)-1]:
		A = V[i]
		for j in [0..len(V)-1]:
			B = V[j]
			M[i,j] = k-len(set(A).intersection(set(B)))
	return association_scheme(base_matrix_to_adjacency_matrices(M))

def GrassmannScheme(q,n,k):
	X = graphs.GrassmannGraph(q,n,k)
	V = X.vertices()
	M = zero_matrix(X.order())
	for i in [0..len(V)-1]:
		A = V[i]
		for j in [0..len(V)-1]:
			B = V[j]
			M[i,j] = k-len(set(A).intersection(set(B)))
	return association_scheme(base_matrix_to_adjacency_matrices(M))

"""def GrassmannScheme(q,n,k):
	V = VectorSpace(GF(q),n)
	D = list(V.subspaces(k))
	M = zero_matrix(len(D))
	for i in [0..len(D)-1]:
		A = D[i]
		for j in [0..len(D)-1]:
			B = D[j]
			M[i,j] = k-(A.intersection(B)).dimension()
	return association_scheme(base_matrix_to_adjacency_matrices(M))"""



def sub_orbits(G): ##need a fix (G is not the automorphism of the resulting graphs)
	S = G.stabilizer(G.domain()[0])
	T = S.orbits()
	T = list(T)
	T.sort()
	symmetric = []
	asymmetric = []
	all_list = []
	for x in T:
		if x[0] == G.domain()[0]:
			break
	T.pop(T.index(x))
	for i in [0..len(T)-1]:
		O = G.orbit(tuple([G.domain()[0],T[i][0]]),"OnPairs")
		X = DiGraph()
		X.add_edges(O)
		A = X.adjacency_matrix()
		all_list.append(X)
		if A.is_symmetric():
			symmetric.append(Graph(X))
		else:
			asymmetric.append(X)
	asymmetric_pairs = []
	for X in asymmetric:
		A = X.adjacency_matrix()
		for B in asymmetric:
			if (A+B.adjacency_matrix()).is_symmetric() and [B.adjacency_matrix(),A] not in asymmetric_pairs:
				asymmetric_pairs.append([X,B])
	return symmetric,asymmetric_pairs

def common_eigenvectors(L):
	eigenspaces_blocks = spectral_decomposition(L[0])
	for i in [1..len(L)-1]:
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
				Ev = spectral_decomposition_of_matrix(B)
				for (y,C) in Ev:
					if y[0] != 0:
						new_eigenspaces_blocks.append((x+y,P*C))
					elif y[0] == 0 and A == B:
						new_eigenspaces_blocks.append((x+y,P*C))
		eigenspaces_blocks = new_eigenspaces_blocks
	return eigenspaces_blocks


def spectral_decomposition_of_matrix(A):
	E = A.right_eigenspaces()
	eigenvalues = [E[i][0] for i in [0..len(E)-1]]
	mats = [E[i][1].matrix() for i in [0..len(E)-1]]
	orthogonal_mats = [x.gram_schmidt()[0] for x in mats]
	spectral_eigenspaces = []
	for i in [0..len(orthogonal_mats)-1]:
		x = orthogonal_mats[i]
		r = x.rows()
		B = zero_matrix(A.dimensions()[0])
		for a in r:
			a = Matrix(a)
			B += a.transpose()*a/(a*a.transpose()).list()[0]
		spectral_eigenspaces.append(([E[i][0]],B))
	return spectral_eigenspaces