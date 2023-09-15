import networkx as nx

node_to_learn = input("Concept to learn: ")

# arbitrary prereqs
G = nx.DiGraph([
    ('Data Types', 'Branching'),
    ('Data Types', 'Variables'),
    ('Branching', 'Conditionals'),
    ('Variables & Operators', 'Functions'),
    ('Data Types', 'Functions'),
    ('Conditionals', 'Functions'),
    ('Functions', 'Recursion'),
])

for sequence in list(nx.all_topological_sorts(G)):
    print(sequence)

print("Descendants:", nx.descendants(G, 'Recursion'))
print("Ancestors:", nx.ancestors(G, 'Recursion'))

print('In degree at Functions:', G.in_degree('Functions'))
print('In degree at Functions:', G.out_degree('Functions'))

# print(f"Topics to learn in order to learn {node_to_learn}:")
# for node in best_sequence:
#     if not node == node_to_learn:
#         print(node)

# DRAWING CODE
# import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 12), dpi=150)
# nx.draw_planar(
#     G,
#     arrowsize=12,
#     with_labels=True,
#     node_size=8000,
#     node_color="#ffff8f",
#     linewidths=2.0,
#     width=1.5,
#     font_size=14,
# )
# plt.show()
