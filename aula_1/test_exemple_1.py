import unittest
from example_1 import generate_duck_names


class TestGenerateDuckNames(unittest.TestCase):

    def test_generate_duck_names(self):
        self.assertEqual(generate_duck_names(letters=prefix), names)


if __name__ == "__main__":
    names =["Jack", "Kack", "Lack", "Mack", "Nack", "Ouack", "Pack", "Quack"]
    prefix = "JKLMNOPQ"
    unittest.main()




