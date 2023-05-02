import randrange
import unittest

class TestRandrange(unittest.TestCase):

    def test_rand_range_param(self):
        self.assertGreaterEqual(randrange.rand_range_param(2, 15), 2)
        self.assertLess(randrange.rand_range_param(2, 15), 15)

        self.assertGreaterEqual(randrange.rand_range_param(10, 200), 10)
        self.assertLess(randrange.rand_range_param(10, 200), 200)

        self.assertGreaterEqual(randrange.rand_range_param(3, 9), 3)
        self.assertLess(randrange.rand_range_param(3, 9), 9)

        self.assertGreaterEqual(randrange.rand_range_param(14, 19), 14)
        self.assertLess(randrange.rand_range_param(14, 19), 19)

if __name__ == '__main__':
    unittest.main()
