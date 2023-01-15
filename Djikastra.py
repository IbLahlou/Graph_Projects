class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {node: float('inf') for node in graph}
        self.previous = {node: None for node in graph}
    
    def find_shortest_path(self, start, end):
        self.distances[start] = 0
        unvisited = set(self.graph)

        while unvisited:
            current = min(unvisited, key=self.distances.get)
            unvisited.remove(current)

            for neighbor, weight in self.graph[current].items():
                potential_distance = self.distances[current] + weight
                if potential_distance < self.distances[neighbor]:
                    self.distances[neighbor] = potential_distance
                    self.previous[neighbor] = current
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.previous[current]
        
        return path[::-1]
        
    def draw_shortest_path(self, path):
        G = nx.Graph()
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos)

        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_labels(G, pos)

        shortest_path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=5)

        plt.show()
