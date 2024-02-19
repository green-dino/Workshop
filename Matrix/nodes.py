import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Function to render the graph and display it in Streamlit
def render_graph(graph):
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=800, font_size=8, edge_color='gray', ax=ax)
    ax.set_title("Node Concepts and Relationships")
    st.pyplot(fig)

# Main Streamlit App
def main():
    st.title("Node Concepts and Relationships Visualization")

    # Initialize the graph using st.session_state (if it doesn't exist)
    if 'graph' not in st.session_state:
        st.session_state.graph = nx.Graph()

    # Sidebar for adding nodes
    st.sidebar.header("Add Node")
    new_node = st.sidebar.text_input("Enter Node Name:")
    if st.sidebar.button("Add Node"):
        st.session_state.graph.add_node(new_node)
        st.sidebar.success(f"Node '{new_node}' added successfully!")

    # Sidebar for adding edges
    st.sidebar.header("Add Edge")
    edge_start = st.sidebar.text_input("Enter Start Node:")
    edge_end = st.sidebar.text_input("Enter End Node:")
    if st.sidebar.button("Add Edge"):
        st.session_state.graph.add_edge(edge_start, edge_end)
        st.sidebar.success(f"Edge added between '{edge_start}' and '{edge_end}'!")

    # Render the graph
    render_graph(st.session_state.graph)

# Run the Streamlit app
if __name__ == "__main__":
    main()
