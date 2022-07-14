from msilib.schema import Error
from numpy import vectorize
from vectors import Vector3
import unittest


class TestVector3Methods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Vector3(1, -5, 3) +
                         Vector3(0, 3, -2), Vector3(1, -2, 1))

    def test_subtract(self):
        self.assertEqual(Vector3(1, 4, -2) -
                         Vector3(-5, 3, 0), Vector3(6, 1, -2))

    def test_multiply(self):
        self.assertEqual(Vector3(1, 4, -2) * 3, Vector3(3, 12, -6))
        self.assertEqual(Vector3(1, 5, -3) *
                         Vector3(-4, 1, 2), Vector3(-4, 5, -6))


if __name__ == '__main__':
    unittest.main()
