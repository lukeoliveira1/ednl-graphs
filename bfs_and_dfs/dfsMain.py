from dfs import Graph, Node
from read_csv import read_csv

if __name__ == "__main__":
    adj = Graph()
    adj.load_from_csv("bfs_and_dfs\grafo.csv")
    adj.display_graph()

    adj.dfs_search(adj.nodes[0], adj.nodes[10], 0, [adj.nodes[0]])
    print(f"Best track: {[node.value for node in adj.best_track]}")
    print(f"Cost: {adj.max_cost}")
