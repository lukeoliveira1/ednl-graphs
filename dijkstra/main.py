from dijkstra import Dijkstra 

if __name__ == "__main__":
    adj = Dijkstra()
    adj.load_from_csv("dijkstra/graph.csv")
    adj.display_graph()

    print(adj.dijkstra("C", "F"))
    adj.visualize_track()