# adjlist = {
#     "A" : ["B","C"],
#     "B" : ["A","D"],
#     "C" : ["A","D","E"],
#     "D" : ["B","C","E"],
#     "E" : ["C","D"]
# }

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

    def add_edge(self, start, end):
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)

    # Degree is the number of edges connected to it
    def degree(self, node):
        return len(self.adj_list[node])


if __name__ == "__main__":

    nodes = ["A", "B", "C", "D", "E"]
    g = Graph(nodes)

    all_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

    for u, v in all_edges:
        g.add_edge(u, v)

    g.print_adj_list()

