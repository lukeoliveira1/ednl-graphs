from bfs import *

if __name__ == "__main__":
    graph = Graph()

    graph.load_from_csv("bfs/grafo2.csv")
    # graph.display_graph()

    # jumps, track = graph.bfs_min_jumps("A", "K")
    # print(f"Jumps: {jumps}")
    # print(f"Track: {track}")

    graph.visualize_paths("B", "G")
