import networkx as nx
import matplotlib.pyplot as plt

# Define the matrices and their relationships
matrices = {
    'A': {'inputs': ['L', 'I'], 'matrix_name': 'Threat Scope', 'result': 'Large'},
    'B': {'inputs': ['I', 'C'], 'matrix_name': 'Protection Capability', 'result': 'Incomplete'},
    'C': {'inputs': ['L', 'I'], 'matrix_name': 'Attack Effectiveness', 'result': 'Consistently'},
    'D': {'inputs': ['P'], 'matrix_name': 'Occurrence', 'result': 'Periodically'},
    'F': {'inputs': ['D', 'E'], 'matrix_name': 'Harm', 'result': 'Damaging'},
    'G': {'inputs': ['E'], 'matrix_name': 'Valuation', 'result': 'Essential'},
    'E': {'inputs': ['C', 'P'], 'matrix_name': 'Threat Likelihood', 'result': 'High Likelihood'},
    'H': {'inputs': ['D', 'E'], 'matrix_name': 'Impact', 'result': 'High Impact'},
    'I': {'inputs': ['HL', 'Hi'], 'matrix_name': 'Risk', 'result': 'High'},
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for matrix_ref, matrix_info in matrices.items():
    G.add_node(matrix_ref, label=f"{matrix_ref}\n{matrix_info['matrix_name']}")

    for input_ref in matrix_info['inputs']:
        G.add_edge(input_ref, matrix_ref)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', arrowsize=20)
plt.title('Matrices and Their Relationships')
plt.show()
