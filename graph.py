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
node_to_learn = 'Recursion' # where to start searching
# TODO: graph is bidirectional right now, should only be one direction; 
# this is evident if you select 'Functions', which would have a prereq to recursion which is wrong

# DFS this graph, pre-order traversal over post for no reason really
nodes = nx.dfs_preorder_nodes(G, node_to_learn)

print(f"Topics to learn in order to learn {node_to_learn}:")
for node in nodes:
    if not node == node_to_learn:
        print(node)

# TODO old code before I realized nx has DFS -- we may need a "custom" DFS though
# path = "" # path to learn the topic
# root_found = False
# while not 'root' in G.adj[node_to_learn].keys():
# while not root_found:

#     print(G.adj[node_to_learn])
#     print(G.adj[node_to_learn].keys())

#     for k, v in G.adj[node_to_learn].items():
#         print("K, V", k, v)
#         if 'edge_label' in v.keys() and v['edge_label'] == 'prerequisiteTo' and not k in searched:
#             path = path + " -> " + k
#             node_to_learn = k
#             searched.append(k)
    
#         print("KEYS:", v.keys())
#         if 'root' in v.keys(): # toggle for next while iteration, because we want to potentially get other prereqs before breaking for root
#             rootFound = True
#             print("root found")

# print("Final path:", path)
