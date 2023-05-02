import logic
import unittest

class TestLogic(unittest.TestCase):

    def test_squirrel_play(self):
        self.assertTrue(logic.squirrel_play(60, False))
        self.assertTrue(logic.squirrel_play(90, False))
        self.assertFalse(logic.squirrel_play(59, False))
        self.assertFalse(logic.squirrel_play(91, False))
        self.assertFalse(logic.squirrel_play(59, True))
        self.assertTrue(logic.squirrel_play(91, True))
        self.assertTrue(logic.squirrel_play(100, True))
        self.assertFalse(logic.squirrel_play(101, True))

    def test_date_fashion(self):
        self.assertEqual(logic.date_fashion(5, 10), 2)
        self.assertEqual(logic.date_fashion(5, 2), 0)
        self.assertEqual(logic.date_fashion(5, 5), 1)

if __name__ == '__main__':
    unittest.main()
