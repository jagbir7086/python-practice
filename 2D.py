import networkx as nx
import numpy as np

a = np.array([[1,-1,0],
              [1,0,0],
              [-1,-1,1]])

G = nx.grid_2d_graph(*a.shape)
list(G.neighbors((0,0)))
# [(1, 0), (0, 1)]