def depthFirstSearch(graph, startVertex):
    visited = []
    stack = [startVertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and i not in visited:
                    stack.append(i)
    return visited
