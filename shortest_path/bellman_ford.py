def bellmanFord(graph, source):
    # Init
    n = len(graph)
    predecessors = [None] * n
    distances = [float("inf")] * n
    distances[source] = 0

    # Main
    stable = False
    i = 0
    while not stable and i < n - 1:
        stable = True
        # Traverse all the edges
        for u in range(n):
            for v in range(n):
                # Update distances
                if graph[u][v] != 0 and distances[v] > distances[u] + graph[u][v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u
                    stable = False
        i += 1

    if not stable and i == n - 1:
        raise Exception("Negative cycle detected. No solution")

    return distances, predecessors
