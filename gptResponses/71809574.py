# To obtain the adjacency matrix for the generated graph, you can use the `nx.adjacency_matrix()` function from the NetworkX library. Here's an updated version of your code that adds the adjacency matrix calculation:

# ```python
import networkx as nx
import numpy as np

n = 10
p = 0.9

G = nx.generators.random_graphs.gnp_random_graph(n, p)
adj_matrix = nx.adjacency_matrix(G)

print(adj_matrix.todense())
# ```

# In this updated code, we first import the `numpy` library to handle matrix operations. Then, we generate the random graph `G` using `gnp_random_graph()`. Finally, the `nx.adjacency_matrix()` function is used to calculate the adjacency matrix, which is stored in the variable `adj_matrix`. The `todense()` method is applied to the adjacency matrix to convert it into a dense matrix form, and it is printed using `print(adj_matrix.todense())`.