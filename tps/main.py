from tps import TPS 

if __name__ == "__main__":
    adj = TPS()
    adj.load_from_csv("tps/graph.csv")
    adj.display_graph()

    adj.tps_dfs("A")

    print("Best track:")
    for i, node in enumerate(adj.best_track):
        if i == len(adj.best_track) - 1:
            print(node.value)
        else:
            print(node.value, end=" -> ")

    adj.visualize_tracks()