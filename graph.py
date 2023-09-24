import networkx as nx
import matplotlib.pyplot as plt

node_to_learn = input("Concept to learn: ")

G = nx.DiGraph([
    ('Data Types', 'Branching'),
    ('Data Types', 'Variables'),
    ('Branching', 'Conditionals'),
    ('Variables', 'Functions'),
    ('Data Types', 'Functions'),
    ('Control Flow', 'Functions'),
    ('Conditionals', 'Functions'),
    ('Functions', 'Recursion'),
    # ('Operators', 'Control Flow'),
    # ('Variables', 'Control Flow'),
    # ('Data Types', 'Control Flow'),
    # ('Variables', 'Tuples'),
    # ('Data Types', 'Tuples'),
    # ('Variables', 'Lists'),
    # ('Data Types', 'Lists'),
    # ('Variables', 'Dictionaries'),
    # ('Data Types', 'Dictionaries'),
    # ('Variables', 'Classes & Objects'),
    # ('Data Types', 'Classes & Objects'),
    # ('Functions', 'Modules'),
    # ('Variables', 'Files'),
    # ('Data Types', 'Files'),
    # ('Functions', 'Files'),
])

# Find all simple paths from any node to 'A'
valid_paths_to_A = list(nx.all_simple_paths(G, source='Data Types', target=node_to_learn))
print(valid_paths_to_A)

sequences = {}
best_sequence = None

for sequence in list(nx.all_topological_sorts(G)):
    print(sequence)

    # TODO speed/length rating is len(sequence) (simple path, not top sort)
    synthesis_rating = 0 # metric of how many in degrees are present
    foundation_rating = 0 # metric of how many out degrees are present

    for node in sequence:
        print(node)
        print(f"in degree of {node}:", G.in_degree(node))
        print(f"out degree of {node}:", G.out_degree(node))
        print()

        synthesis_rating += G.in_degree(node)
        foundation_rating += G.out_degree(node)

# print("Ancestors:", nx.ancestors(G, 'Recursion')) # TODO uninclude ancestor nodes?

# best_sequence = ['Data Types', 'Variables & Operators', 'Branching', 'Variables', 'Conditionals', 'Functions', 'Recursion']
# print(f"Sequence of topics to learn in order to learn {node_to_learn}:")
# for node in best_sequence:
#     if not node == node_to_learn:
#         print(node)

# draw the graph
plt.figure(figsize=(12, 12), dpi=150)
nx.draw_planar(
    G,
    arrowsize=12,
    with_labels=True,
    node_size=8000,
    node_color="#ffff8f",
    linewidths=2.0,
    width=1.5,
    font_size=14,
)
plt.show()
