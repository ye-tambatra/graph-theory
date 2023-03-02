def depthFirstSearch(graph, startVertex):
    visited = []
    queue = [startVertex]
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and i not in visited:
                    queue.append(i)
    return visited
