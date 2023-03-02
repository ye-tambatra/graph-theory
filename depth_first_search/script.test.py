from script import depth_first_search
import unittest


class DepthFirstSearchTest(unittest.TestCase):
    def test_depth_first_search(self):
        graph = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        traversal_order = [0, 1, 3, 2]
        self.assertEqual(depth_first_search(graph, 0), traversal_order)


if __name__ == "__main__":
    unittest.main()
