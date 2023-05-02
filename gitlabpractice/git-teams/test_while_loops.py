import while_loops
import unittest

class TestWhileLoops(unittest.TestCase):

    def test_while2(self):
        self.assertEqual(while_loops.while2(3,4), 19)
        self.assertEqual(while_loops.while2(2,5), 22)
        self.assertEqual(while_loops.while2(18,3), 18)

    def test_while11(self):
        self.assertEqual(while_loops.while11([1,1,1,1,1,1,1,1,1], 6), 7)
        self.assertEqual(while_loops.while11([2,2,2,2,2,2,2,2,2], 6), 8)

if __name__ == '__main__':
    unittest.main()
