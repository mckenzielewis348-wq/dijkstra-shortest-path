import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes[v] = []
        self.nodes[u].append((v, weight))

    def shortest_path(self, start, target):
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            (cost, current, path) = heapq.heappop(pq)

            if current in visited:
                continue
            
            visited.add(current)

            if current == target:
                return cost, path

            for neighbor, weight in self.nodes.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

        return float("inf"), []
