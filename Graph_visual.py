import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(matrix, graph_create_using, label_dict):
    adj_matrix = np.array(matrix)
    G = nx.from_numpy_array(adj_matrix, create_using=graph_create_using)
    G = nx.relabel_nodes(G, label_dict)
    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, arrows=True, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '1' for u, v in G.edges()})
    plt.title("Graph Visualization from Adjacency Matrix")
    plt.show()
