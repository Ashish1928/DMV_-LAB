import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices: "))

if n <= 3:
    print("Number of vertices must be greater than 3!!")
else:
    # Create a complete graph with n vertices
    G = nx.complete_graph(n)

    print("\nEdges of the complete graph:")
    print(list(G.edges()))

    # Draw the graph
    nx.draw(
        G,
        with_labels=True,
        node_color='lightblue',
        node_size=800,
        font_size=10
    )

    plt.title(f"Complete graph with {n} vertices")
    plt.show()
