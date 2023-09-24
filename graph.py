import networkx as nx
import matplotlib.pyplot as plt
from nm_data import notional_machines

def get_nm_topics() -> list[str]:
    return list(set([notional_machines[notional_machine]['Topic'] for notional_machine in notional_machines]))

def get_nms_by_topic(topic: str) -> list[str]:
    found_nms = []
    for notional_machine in notional_machines:
        if topic == notional_machines[notional_machine]['Topic']:
            found_nms.append(notional_machine)
    return found_nms

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

from dataclasses import dataclass

@dataclass
class Sequence:
    synthesis_rating: int = 0
    foundation_rating: int = 0
    path = None

    def __init__(self, synthesis_rating, foundation_rating, path):
        self.synthesis_rating = synthesis_rating
        self.foundation_rating = foundation_rating
        self.path = path

sequences = []

simple_paths = list(nx.all_simple_paths(G, source='Data Types', target=node_to_learn))
for path in simple_paths:
    synthesis_rating = 0 # metric of how many in degrees are present
    foundation_rating = 0 # metric of how many out degrees are present

    for node in path:
        synthesis_rating += G.in_degree(node)
        foundation_rating += G.out_degree(node)
    
    sequences.append(Sequence(synthesis_rating, foundation_rating, path))

best_sequence = None # TODO decide best sequence

for sequence in sequences:
    print(sequence.path)
    print("SYNTHESIS:", sequence.synthesis_rating)
    print("FOUNDATION:", sequence.foundation_rating)
    print("PATH LEN:", len(sequence.path))
    print()

for sequence in list(nx.all_topological_sorts(G)):
    print(sequence)

# Draw the graph
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
