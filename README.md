# association-schemes package

This is a Sagemath package for association schemes. To load the package, just type the following in a terminal.

```  sage
sage: load("https://raw.githubusercontent.com/sarobidy19/association-schemes/refs/heads/main/code.sage")
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
- ``intersection_number()``
- ``is_commutative()``
- ``is_schurian()``
- ``automorphism_group()``
- ``character_table()``
