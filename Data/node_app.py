# Import necessary libraries
import streamlit as st
from pyvis.network import Network
import re

# Function to create and display the network graph
def display_network_graph(nodes, edges):
    # Create a network instance
    net = Network(height="500px", width="100%", notebook=True)

    # Add nodes and edges to the network
    net.add_nodes(nodes)
    
    for edge in edges:
        # Split each edge by any non-alphanumeric characters
        edge_nodes = re.split(r'\W+', edge)
        if len(edge_nodes) == 2:
            net.add_edge(edge_nodes[0], edge_nodes[1])

    # Display the network graph
    net.show("network.html")

    # Display the HTML file using Streamlit
    st.components.v1.html(open("network.html", 'r').read(), height=600, width=800)

# Main Streamlit app
def main():
    st.title("Learning Nodes and Edges")

    # Sidebar for user input
    st.sidebar.header("Graph Configuration")

    # User input for nodes and edges
    nodes_input = st.sidebar.text_area("Enter nodes (comma-separated)", "Node1, Node2, Node3")
    edges_input = st.sidebar.text_area("Enter edges (comma-separated)", "Node1-Node2, Node2-Node3")

    # Convert user input to lists
    nodes = [node.strip() for node in nodes_input.split(",")]
    edges = [edge.strip() for edge in edges_input.split(",")]

    # Display the network graph
    display_network_graph(nodes, edges)

# Run the Streamlit app
if __name__ == "__main__":
    main()
