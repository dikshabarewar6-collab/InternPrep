# Graph basics
# Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

print(graph)

# Traverse Graph

for node in graph:
    print(node, "→", graph[node])