from depth_first_search import depthFirstSearch
from breadth_first_search import breadthFirstSearch
import unittest


class TestGraphTraversal(unittest.TestCase):
    def setUp(self):
        self.adjacencyMatrix = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]

    def testDepthFirstSearch(self):
        traversalOrder = [0, 1, 3, 2]
        self.assertEqual(depthFirstSearch(self.adjacencyMatrix, 0), traversalOrder)

    def testBreadthFirstSearch(self):
        traversalOrder = [0, 1, 2, 3]
        self.assertEqual(breadthFirstSearch(self.adjacencyMatrix, 0), traversalOrder)


if __name__ == "__main__":
    unittest.main()
