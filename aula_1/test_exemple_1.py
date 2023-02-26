import unittest
from example_1 import prefix_and_suffix, names




class TestPrefixAndSuffix(unittest.TestCase):

    def test_prefix_and_suffix(self):
        self.assertEqual(prefix_and_suffix(), names)


if __name__ == "__main__":
    unittest.main()
