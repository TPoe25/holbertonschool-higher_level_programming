#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        with self.assertRaises(ValueError):
            b5 = Base(0)

        with self.assertRaises(ValueError):
            b6 = Base(-1)

        with self.assertRaises(TypeError):
            b7 = Base("invalid")

if __name__ == '__main__':
    unittest.main()
