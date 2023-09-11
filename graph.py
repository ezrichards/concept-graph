import networkx as nx

# G.add_nodes_from([
#     'Variables & Operators',
#     'Data Types',
#     'Branching',
#     'Conditionals',
#     'While Loops',
#     'For Loops',
#     'Nested Logic',
#     'Functions',
#     'File I/O',
#     'Recursion',
#     'Classes'
# ])

node_to_learn = input("Concept to learn: ")

# arbitrary prereqs
G = nx.DiGraph([
    ('Data Types', 'Branching'),
    ('Branching', 'Conditionals'),
    ('Variables & Operators', 'Functions'),
    ('Data Types', 'Functions'),
    ('Conditionals', 'Functions'),
    ('Functions', 'Recursion'),
])

for sequence in list(nx.all_topological_sorts(G)):
    print(sequence)

    # print(f"Topics to learn in order to learn {node_to_learn}:")
    # for node in nodes:
    #     if not node == node_to_learn:
    #         print(node)

# predecessors/parent nodes: https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.predecessors.html
# successor/child nodes: https://networkx.org/documentation/networkx-1.10/reference/generated/networkx.DiGraph.successors.html 

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
