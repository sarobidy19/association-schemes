
#from sage.groups.perm_gps.permgroup import PermutationGroup_generic
#from  import PermutationGroup_action
#from sage.graphs.digraph import DiGraph
#from sage.combinat.subset import Subsets

class PermutationGroup(PermutationGroup_generic):

	def is_derangement(self,x):
		"""
		Return whether ``self`` is a derangement.

		EXAMPLE:

		.. code-block:: sage

				sage: G = PermutationGroup(SymmetricGroup(5).gens())
				sage: G.is_derangement(G((1,5,2)))
				False
				sage: G.is_derangement(G("(1,5,2)(3,4)"))
				True

		"""
		if 1 in x.cycle_type():
			return False
		else:
			return True
	def number_of_derangements(self):
		"""
		Return the number of derangements in ``self``.

		"""
		cc = self.conjugacy_classes_representatives()
		D = []
		for x in cc:
			if self.is_derangement(x):
				D.append(x)
		Der = []
		for x in D:
		    Der += self.conjugacy_class(x).list()
		return len(Der)

	def action_on_subsets(self,k):
		"""
		Return the action of ``self`` on the ``k``-sets of ``self.domain()``.

		EXAMPLE:

		.. code-block:: sage

		sage: G = PermutationGroup(SymmetricGroup(5).gens())
		sage: K = G.action_on_subsets(2)
		sage: K.is_transitive()
		True


		"""
		n = self.degree()
		S = self.gens_small()
		G = self.subgroup(S)
		action_on_subsets = lambda h,y: frozenset([h(z) for z in y])
		V = Subsets(self.domain(),k)
		H = sage.groups.perm_gps.permgroup.PermutationGroup_action(S, action = action_on_subsets,domain=[frozenset(v) for v in V])
		return PermutationGroup(H.minimal_generating_set())

	def rank_of_group(self):
		return len(self.stabilizer(self.domain()[0]).orbits())

	def group_action(self,H):
		C = self.cosets(H,side="left")
		D = [frozenset(x) for x in C]
		action_on_object = lambda g,x: frozenset([g*y for y in x])
		G  = PermutationGroup_action(self.gens(),action = action_on_object,domain=D)
		return PermutationGroup(G.gens())

	def stabilizer_of_invariant_partition(self,L):
	    N = []
	    Perms = []
	    #L = self.blocks_all()[0]
	    L = self.orbit(tuple(L),"OnSets")
	    for x in L:
	        N.append(self.stabilizer(tuple(x),"OnSets"))
	    x = set(N[0])
	    for s in N:
	        x = set(s).intersection(x)
	    return permutation_group(PermutationGroup(list(x)))

	def sub_orbits(self,v):
		G = self
		S = G.stabilizer(v)
		O = S.orbits()
		return O

	def orbital_digraphs(self):
		G = self
		v = G.domain()[0]
		O = G.sub_orbits(v)
		Digraphs = []
		for x in O:
			if x[0]!= v:
				X = DiGraph()
				X.add_vertices(G.domain())
				X.add_edges(G.orbit((v,x[0]),"OnTuples"))
				Digraphs.append(X)
		return Digraphs

	def pointwise_stabilizer(self,S):
		T = self
		for x in S:
			T = T.intersection(self.stabilizer(x))
		return T

	def setwise_stabilizer(self,S):
		return self.stabilizer(tuple(S),"OnSets")

	def is_quasi_primitive(self):
		L = self.normal_subgroups()
		for H in L:
			if H.order()>1 and H.is_transitive() == False:
				return False
			else:
				pass
		return True

	def permutation_character(self):
		return self.stabilizer(self.domain()[0]).trivial_character().induct(self)

	def is_core_free(self,H):
		L = H.conjugacy_classes_subgroups()
		for x in L:
			if x.is_normal(self):
				return False
			else:
				pass
		return True
