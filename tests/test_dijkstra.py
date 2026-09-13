from dijkstra.graph import Graph

def test_shortest_path():
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)

    cost, path = g.shortest_path('A', 'E')
    assert cost == 11
    assert path == ['A', 'B', 'D', 'E']
