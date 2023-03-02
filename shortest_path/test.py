from moore_dijkstra import mooreDijkstra
import unittest


class TestShortestPath(unittest.TestCase):
    def testMooreDijkstra(self):
        adjacencyMatrix = [
            [0, 6, 0, 1, 0],
            [6, 0, 5, 2, 2],
            [0, 5, 0, 0, 5],
            [1, 2, 0, 0, 1],
            [0, 2, 5, 1, 0],
        ]
        expectedDistances, expectedPredecessors = [0, 3, 7, 1, 2], [None, 3, 4, 0, 3]
        distances, predecessors = mooreDijkstra(adjacencyMatrix, 0)
        self.assertEqual(distances, expectedDistances)
        self.assertEqual(predecessors, expectedPredecessors)


if __name__ == "__main__":
    unittest.main()
