import strings
import unittest

class TestStrings(unittest.TestCase):

    def test_without_end(self):
        self.assertEqual(strings.without_end('Hello'), 'ell')
        self.assertEqual(strings.without_end('java'), 'av')
        self.assertEqual(strings.without_end('coding'), 'odin')

    def test_partstring2(self):
        self.assertEqual(strings.partstring2("Call me Ishmael.", 8, 2), "Ihal")
        self.assertEqual(strings.partstring2("abcdefghijklmnop", 8, 3), "ilo")

    def test_in1to10(self):
        self.assertTrue(strings.in1to10(5, False))
        self.assertFalse(strings.in1to10(11, False))
        self.assertTrue(strings.in1to10(11, True))

    def test_missing_char(self):
        self.assertEqual(strings.missing_char("fred", 0), "red")
        self.assertEqual(strings.missing_char("fred", 1), "fed")
        self.assertEqual(strings.missing_char("fred", 2), "frd")
        self.assertEqual(strings.missing_char("fred", 3), "fre")

    def test_first_two(self):
        self.assertEqual(strings.first_two('Hello'), 'He')
        self.assertEqual(strings.first_two('abcdefg'), 'ab')
        self.assertEqual(strings.first_two('ab'), 'ab')

    def test_cat_dog(self):
        self.assertTrue(strings.cat_dog('catdog'))
        self.assertFalse(strings.cat_dog('catcat'))
        self.assertTrue(strings.cat_dog('1cat1cadodog'))

if __name__ == '__main__':
    unittest.main()
