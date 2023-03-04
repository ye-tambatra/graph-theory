def floydWarshall(graph):
    # Init
    n = len(graph)
    distances = [[float("inf") for i in range(n)] for j in range(n)]
    predecessors = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            # Init the distances and the predecessors
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != 0:
                distances[i][j] = graph[i][j]
                predecessors[i][j] = i

    # Main
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Updating the distances
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    predecessors[i][j] = predecessors[k][j]

    return (distances, predecessors)
