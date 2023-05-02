import lists
import unittest

class TestLists(unittest.TestCase):

    def test_common_end(self):
        self.assertTrue(lists.common_end([1, 2, 3], [7, 3]))
        self.assertFalse(lists.common_end([1, 2, 3], [7, 3, 2]))
        self.assertTrue(lists.common_end([1, 2, 3], [1, 3]))

    def test_laststring(self):
        self.assertEqual(lists.laststring(["a","b","c","d"]), "d")

    def test_middlelist(self):
        self.assertListEqual(lists.middlelist([ 2, 3, 5, 7, 11, 13 ], 1, 4), [ 3, 5, 7 ])
        self.assertListEqual(lists.middlelist([ 2, 3, 5, 7, 11, 13 ], 2, 5), [ 5, 7, 11 ])

    def test_centered_average(self):
        self.assertEqual(lists.centered_average([1, 2, 3, 4, 100]), 3)
        self.assertEqual(lists.centered_average([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(lists.centered_average([-10, -4, -2, -4, -2, 0]), -3)

    def test_count_evens(self):
        self.assertEqual(lists.count_evens([2, 1, 2, 3, 4]), 3)
        self.assertEqual(lists.count_evens([2, 2, 0]), 3)
        self.assertEqual(lists.count_evens([1, 3, 5]), 0)

if __name__ == '__main__':
    unittest.main()
