from pyvis.network import Network

# Create a network
net = Network(notebook=True)

# Add nodes representing food items
net.add_nodes(
    [1, 2, 3, 4, 5, 6],
    label=["Pizza", "Sushi", "Burger", "Salad", "Ice Cream", "Tacos"],
    color=["#ff8000", "#0099ff", "#ff0000", "#00cc00", "#cc00cc", "#ffff00"],
)

# Add edges representing relationships between food items
net.add_edge(1, 5, value=2)  # Pizza and Ice Cream have a strong connection
net.add_edges([(2, 5, 5), (3, 4, 2), (1, 6), (2, 6), (3, 5)])

# Visualize the network
net.show("food_network.html")
