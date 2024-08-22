import networkx as nx

class MetroNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_station(self, station):
        self.graph.add_node(station)

    def add_connection(self, station1, station2, distance):
        self.graph.add_edge(station1, station2, distance=distance)

    def shortest_path(self, source, target):
        try:
            return nx.shortest_path(self.graph, source=source, target=target, weight='distance')
        except nx.NetworkXNoPath:
            return f"No path found between {source} and {target}."

    def simulate(self):
        pass

    def optimize_schedule(self):
        pass

    def get_stations(self):
        return list(self.graph.nodes)

    def get_connections(self):
        return list(self.graph.edges.data('distance'))
