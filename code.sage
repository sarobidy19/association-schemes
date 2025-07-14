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
			eigenvalues,idempotents = self.spectral_decomposition()
			L = self.adjacency_matrices()
			r = self.rank()
			for i in [0..r-1]:
				row = []
				E = idempotents[i]
				for j in [0..r-1]:
					A = L[j]
					u = E.column(0)
					v = A*u
					for k in [0..len(u)-1]:
						if u[k] != 0:
							eigenvalue = v[k]/u[k]
							break
					row.append(eigenvalue)
				table.append(row)
			return Matrix(table)





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

def orbital_scheme_of_transitive_group(G):
	S = sub_orbits(G)
	A = association_scheme([matrix.identity(G.degree())]+[x.adjacency_matrix() for x in S[0]]+[x[0].adjacency_matrix() for x in S[1]])
	return A

def orbital_scheme_of_group_action(G):
	H = G.stabilizer(G.domain()[0])
	K = group_action_on_cosets(G,H)
	S = sub_orbits(K)
	A = association_scheme([matrix.identity(K.degree())]+[x.adjacency_matrix() for x in S[0]]+[x[0].adjacency_matrix() for x in S[1]])
	return A

