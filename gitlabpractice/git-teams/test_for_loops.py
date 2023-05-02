import unittest
import for_loops

class TestForLoops(unittest.TestCase):

    def test_find_char_1(self):
        self.assertListEqual(for_loops.find_char("thistheother", "t"), [0, 4, 8])

    def test_find_char_2(self):
        self.assertListEqual(for_loops.find_char("duranduransnewalbumisgood", "d"), [0, 5, 24])

    def test_find_char_3(self):
        self.assertListEqual(for_loops.find_char("thistheother", "o"), [7])

if __name__ == '__main__':
    unittest.main()
