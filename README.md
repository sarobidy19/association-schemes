# association-schemes package

This is a Sagemath package for association schemes. To load the package, just type the following in a terminal.

```  sage
load("https://raw.githubusercontent.com/sarobidy19/association-schemes/refs/heads/main/code.sage")
```
### Generic association schemes
An association scheme in the association-schemes package is defined by giving the adjacency matrices corresponding to the relations.

```  sage
association_scheme(adjacency_matrices)
INPUT:
 - adjacency_matrices: a list of 01-matrices forming an association scheme.
OUTPUT:
  A class called association_scheme.
```

**Example:** The Johnson scheme J(5,2) can be obtained as follows.
``` sage
sage: X = graphs.PetersenGraph()
sage: A = X.adjacency_matrix()
sage: B = X.complement().adjacency_matrix()
sage: I = matrix.identity(X.order())
sage: AS = association_scheme([I,A,B])
```

### Methods

- ``order()``
    
    Return the number of vertices in self.

    ```  sage
    sage: X = graphs.PetersenGraph()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
    sage: AS.order()
    10

    ```
- ``rank()``
  
    Return the number of relations in self.
  
    ```  sage
    sage: X = graphs.PetersenGraph()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
    sage: AS.rank()
    3
    ```
- ``adjacency_matrices()``
  
    Return the adjacency matrices of self as a list.
    ```  sage
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
    ```
- ``base_matrix()``
  
    Return the base matrix of self. If $`(\Omega,\mathcal{R})`$ is an association scheme with adjacency matrices $A_0 = I, A_1,\ldots, A_d$, then the *base matrix* of $(\Omega,\mathcal{R})$ is the matrix
    $0A_0 + 1A_1+2A_2+ \ldots+ dA_d$.

    ```  sage
    sage: X = graphs.PetersenGraph()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
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
    ```
- ``intersection_number(i,j,k)``

    Return the intersection number $p_{ij}^k$ of the association scheme ``self``.

    
    INPUT: integers $i,j,$ and $k$ between $0$ and the $r$, where $r+1$ is the rank of the association scheme.

    OUTPUT: the value of $p_{ij}^k$.
    
    EXAMPLE:

    For example, the intersection numbers of the affine polar graph $VO_6^-(2)$ can be computed as follows.

    ``` sage
        sage: X = graphs.AffineOrthogonalPolarGraph(6,2,sign="-")
        sage: A = X.adjacency_matrix()
        sage: B = X.complement().adjacency_matrix()
        sage: I = matrix.identity(X.order())
        sage: AS = association_scheme([I,A,B])
        sage: AS.intersection_number(0,1,1)
        1
        sage: AS.intersection_number(1,1,1)
        10
        sage: AS.intersection_number(2,2,1)
        20
        sage: AS.intersection_number(2,2,2)
        20
    ```

- ``is_commutative()``

    Return whether or not ``self`` is a commutative association scheme.

    The $d$-class assocition scheme $(\Omega,\mathcal{R})$ is commutative if its intersection numbers satisfy $p_{ij}^k = p_{ji}^k$, for all $0\leq i,j,k\leq d$. 

    EXAMPLE:

    ```sage
    sage: AS = OrbitalSchemeTransitiveGroup(group_acting_on_subsets(PSL(2,7),2))
    sage: AS.is_commutative()
    False
    sage: AS = OrbitalSchemeTransitiveGroup(group_acting_on_subsets(AlternatingGroup(7),2))
    sage: AS.is_commutative()
    True

    ```

- ``is_schurian()``

    Return whether or not ``self`` is Schurian, that is, its relations are the orbital of a transitive group

    EXAMPLE: 

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: AS1 = OrbitalSchemeTransitiveGroup(G)
    sage: AS1.is_schurian()
    True
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS2 = association_scheme([I,A,B])
    sage: AS2.is_schurian()
    False
    ```

- ``automorphism_group()``

    Return the automorphism group of ``self``, that is, the permutation group that preserves all relations of ``self``.

    EXAMPLE:

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
    sage: K = AS.automorphism_group()
    sage: K.structure_description()
    '(((C4 x C4) : C3) : C2) : C2'
    sage: K.is_transitive()
    True
    ```
- ``character_table()``

    Return the first eigenmatrix of `self`.

    EXAMPLE:

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
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
    ```



- ``P_matrix()``

    Return the first eigenmatrix of `self`. This is the same as `character_table()`.


- ``Q_matrix()``

    Return the first eigenmatrix of `self`.

    EXAMPLE:

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
    sage: AS.Q_matrix()()
    [ 1  6  9]
    [ 1  2 -3]
    [ 1 -2  1]
    sage: AS1 = OrbitalSchemeTransitiveGroup(G)
    sage: AS1.Q_matrix()()
    [ 1  6  3  6]
    [ 1  2 -1 -2]
    [ 1 -2 -1  2]
    [ 1 -2  3 -2]
    ```
- ``is_formally_self_dual()``

    Return whether `self` is formally self dual. That is, whether $Q = \overline(P)$.

    EXAMPLE: 

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: A = X.adjacency_matrix()
    sage: B = X.complement().adjacency_matrix()
    sage: I = matrix.identity(X.order())
    sage: AS = association_scheme([I,A,B])
    sage: AS1 = OrbitalSchemeTransitiveGroup(G)
    sage: AS.is_formally_self_dual()
    True
    sage: AS1.is_formally_self_dual()
    False
    ```

- ``TerwilligerAlgebra(vertex,ring=CC)``

    Return the Terwilliger algebra, over `ring`, of `self` with respect to `vertex`.

    EXAMPLE:

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: AS = OrbitalSchemeTransitiveGroup(G)
    sage: T = AS.TerwilligerAlgebra(1,ring=CC)
    sage: T
    Free module generated by {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30} over Complex Field with 53 bits of precision
    sage: T.dimension()
    31
    ```

- ``dimension_of_t_zero(matrix = False)``

    Return the dimension of the subspace $T_0$ of the Terwilliger algebra with respect to any vertex.

    ```sage
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
    ```

- ``dimension_of_centralizer_algebra(vertex,matrix=False)``

    Return the dimension of the centralizer algebra of the stabilizer of `vertex` in the automorphism group of `self` if `matrix=False`. If `matrix=True`, then it returns the block dimension decomposition of the centralizer algebra.

    EXAMPLE:

    ```sage
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
    ```    

- ``graphs_in_scheme()``
    
    Return the graphs corresponding to symmetric classes of `self`.

    EXAMPLE:

    ```sage
    sage: X = graphs.ShrikhandeGraph()
    sage: G = X.automorphism_group()
    sage: AS = OrbitalSchemeTransitiveGroup(G)
    sage: AS.graphs_in_scheme()
    [Graph on 16 vertices, Graph on 16 vertices, Graph on 16 vertices]
    ```     

- ``ratio_bound(i)``

    Return the value of Hoffman's ratio bound for the i-th graph, if it is symmetric.

    EXAMPLE:

    ```sage
    sage: AS = JohnsonScheme(8,3)
    sage: AS.ratio_bound(0)
    '... the index needs to be larger than 0'
    sage: AS.ratio_bound(1)
    28/3
    sage: AS.ratio_bound(2)
    8
    sage: AS.ratio_bound(3)
    21
    ``` 
