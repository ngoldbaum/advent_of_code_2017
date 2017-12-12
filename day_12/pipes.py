import networkx as nx
import matplotlib.pyplot as plt

with open('input', 'r') as f:
    text = f.readlines()

G = nx.Graph()

for line in text:
    node, neighbors = line.strip().split(' <-> ')

    G.add_edges_from([(node, neighbor) for neighbor in neighbors.split(', ')])

nx.draw(G, node_size=5)
plt.savefig('graph.png')

print(len(nx.node_connected_component(G, '0')))
print(nx.number_connected_components(G))
