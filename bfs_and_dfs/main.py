def read_csv(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip().split(",")
        return lines


print(read_csv("bfs_and_dfs\grafo.csv"))
