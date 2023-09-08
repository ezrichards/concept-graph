import networkx as nx

G = nx.Graph()

G.add_nodes_from([
    'Variables & Operators',
    'Data Types',
    'Branching',
    'Conditionals',
    'While Loops',
    'For Loops',
    'Nested Logic',
    'Functions',
    'File I/O',
    'Recursion',
    'Classes'
])

# some arbitrary prereqs I made
G.add_edge('Data Types', 'Branching', edge_label="prerequisiteTo")
G.add_edge('Branching', 'Conditionals', edge_label='prerequisiteTo')

G.add_edge('Variables & Operators', 'Functions', edge_label="prerequisiteTo", root=True)
G.add_edge('Data Types', 'Functions', edge_label='prerequisiteTo')
G.add_edge('Conditionals', 'Functions', edge_label='prerequisiteTo')
G.add_edge('Functions', 'Recursion', edge_label='prerequisiteTo')

visited = [] # searched nodes
node_to_learn = input()
# TODO: graph is bidirectional right now, should be a DAG

# DFS this graph, pre-order traversal over post for no reason really
nodes = nx.dfs_preorder_nodes(G, node_to_learn)

print(f"Topics to learn in order to learn {node_to_learn}:")
for node in nodes:
    if not node == node_to_learn:
        print(node)
