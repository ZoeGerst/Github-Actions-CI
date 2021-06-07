import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_mul(self):
        self.assertEqual(example.mul(3, 4), 12)

    def test_div(self):
        self.assertEqual(example.div(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
