import json
from dijkstra.graph import Graph

def load_graph_from_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    g = Graph()
    for edge in data['edges']:
        g.add_edge(edge['from'], edge['to'], edge['weight'])
        
    return g, data['start_node'], data['target_node']

if __name__ == "__main__":
    graph, start, target = load_graph_from_json('graph_data.json')
    cost, path = graph.shortest_path(start, target)
    print(f"Shortest Path: {' -> '.join(path)}")
    print(f"Total Cost: {cost}")
