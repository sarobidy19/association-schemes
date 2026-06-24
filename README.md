# AssociationSchemesSagemath package

This is a Sagemath package for association schemes and related objects.


## How to use AssociationSchemesSagemath
To load the package, just type the following in a sage prompt.


```python
load("https://raw.githubusercontent.com/sarobidy19/association-schemes/refs/heads/main/AssociationSchemes/load_package.py")
```

Association schemes are defined using adjacency matrices. An example of a generic association scheme is given below.

```python
sage: X = graphs.PetersenGraph()
sage: A = X.adjacency_matrix()
sage: B = X.complement().adjacency_matrix()
sage: I = matrix.identity(X.order())
sage: AS = AssociationScheme([I,A,B])

```



## Documentation

Click [here](https://sarobidyraz.com/association-schemes/) for the documentation.
