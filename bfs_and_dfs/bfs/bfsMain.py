from bfs import *

if __name__ == "__main__":
    adj = Graph()

    adj.load_from_csv("bfs_and_dfs/bfs/grafo2.csv")
    adj.print_adjacency_list()
    
    jumps, track = adj.bfs_min_jumps("A", "K")
    print(f"Jumps: {jumps}")
    print(f"Track: {track}")

 
