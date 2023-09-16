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

sequences = {}
best_sequence = None

for sequence in list(nx.all_topological_sorts(G)):
    print(sequence)

    synthesis_rating = 0 # metric of how many in degrees are present
    foundation_rating = 0 # metric of how many out degrees are present

    for node in sequence:
        print()
        print("NODE N", node)
        print(f"in degree of {node}:", G.in_degree(node))
        print(f"out degree of {node}:", G.out_degree(node))
        print()

        synthesis_rating += G.in_degree(node)
        foundation_rating += G.out_degree(node)

    print("SYNTHESIS:", synthesis_rating)
    print("FOUNDATIONS:", foundation_rating)

# TODO uninclude ancestor nodes?
print("Descendants:", nx.descendants(G, 'Recursion'))
print("Ancestors:", nx.ancestors(G, 'Recursion'))

# TODO update this, hardcoded for now
best_sequence = ['Data Types', 'Variables & Operators', 'Branching', 'Variables', 'Conditionals', 'Functions', 'Recursion']
print(f"Sequence of topics to learn in order to learn {node_to_learn}:")
for node in best_sequence:
    if not node == node_to_learn:
        print(node)

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
