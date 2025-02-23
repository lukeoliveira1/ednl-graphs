from classes import *

if __name__ == "__main__":
    adj = AdjacentNodesLists()
    for i in range(1, 10):
        adj.insert(i)

    adj.add_edge(1, 2)
    adj.add_edge(1, 4)
    adj.add_edge(2, 3)
    adj.add_edge(2, 5)
    adj.add_edge(3, 6)
    adj.add_edge(3, 5)
    adj.add_edge(4, 5)
    adj.add_edge(5, 7)
    adj.add_edge(6, 7)
    adj.add_edge(7, 8)
    adj.add_edge(5, 9)
    adj.add_edge(7, 9)

    print(adj.bfs_min_jumps(1, 5))

    # adj.print_adjacency_list()
