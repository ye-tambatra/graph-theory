from moore_dijkstra import mooreDijkstra
from bellman_ford import bellmanFord
from floyd_warshall import floydWarshall
import unittest


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        # Graph with positive distances
        self.adjacencyMatrix = [
            [0, 6, 0, 1, 0],
            [6, 0, 5, 2, 2],
            [0, 5, 0, 0, 5],
            [1, 2, 0, 0, 1],
            [0, 2, 5, 1, 0],
        ]
        self.expectedDistances = [0, 3, 7, 1, 2]
        self.expectedPredecessors = [None, 3, 4, 0, 3]
        # Graph with negative distances
        self.adjacencyMatrix1 = [
            [0, 4, 0, 5],
            [0, 0, 0, 0],
            [0, -10, 0, 0],
            [0, 0, 3, 0],
        ]
        self.expectedDistances1 = [0, -2, 8, 5]
        self.expectedPredecessors1 = []

    def testMooreDijkstra(self):
        # A positive distances should work normally
        distances, predecessors = mooreDijkstra(self.adjacencyMatrix, 0)
        self.assertEqual(distances, self.expectedDistances)
        self.assertEqual(predecessors, self.expectedPredecessors)
        # Negative distances should not be supported
        with self.assertRaises(Exception):
            mooreDijkstra(adjacencyMatrix1, 0)

    def testBellmanFord(self):
        # A positive distances should work normally
        distances, predecessors = bellmanFord(self.adjacencyMatrix, 0)
        self.assertEqual(distances, self.expectedDistances)
        self.assertEqual(predecessors, self.expectedPredecessors)
        # Negative distances should be also supported
        distances, predecessors = bellmanFord(self.adjacencyMatrix1, 0)
        self.assertEqual(distances, self.expectedDistances1)

    def testFloydWarshall(self):
        adjacencyMatrix = [[0, 3, 0, 7], [8, 0, 2, 0], [5, 0, 0, 1], [2, 0, 0, 0]]
        expectedDistances = [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]
        expectedPredecessors = [
            [None, 0, 1, 2],
            [3, None, 1, 2],
            [3, 0, None, 2],
            [3, 0, 1, None],
        ]
        distances, predecessors = floydWarshall(adjacencyMatrix)
        self.assertEqual(distances, expectedDistances)
        self.assertEqual(predecessors, expectedPredecessors)


if __name__ == "__main__":
    unittest.main()
