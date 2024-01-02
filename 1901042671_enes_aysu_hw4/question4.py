def exhaustive_search(graph, source, destination):
    min_latency = float('inf')
    min_latency_path = []

    def dfs(current_node, current_path, current_path_latency):
        nonlocal min_latency, min_latency_path

        if current_node == destination:
            if current_path_latency < min_latency:
                min_latency = current_path_latency
                min_latency_path[:] = current_path

        for neighbor, edge_latency in graph[current_node].items():
            if neighbor not in current_path:
                new_latency = current_path_latency + edge_latency
                dfs(neighbor, current_path + [neighbor], new_latency)

    dfs(source, [source], 0)

    return min_latency_path

# example 
start_node = 'A'
final_node = 'C'

graph = {'A': {'B': 2, 'C': 5},
         'B': {'A': 2, 'C': 1},
         'C': {'A': 5, 'B': 1}}

result_path = exhaustive_search(graph, start_node, final_node)
print(f"Minimum latency path from {start_node} to {final_node}: {result_path}")
