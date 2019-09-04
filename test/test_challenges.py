import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from challenge_one import odds


class TestChallenge(unittest.TestCase):

    def test_challenge_one(self):
        self.assertEqual(odds([0, 1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(odds(['Matt', 'Andy', 'Tom', 'Jeremy']), 
                              ['Andy', 'Jeremy'])


if __name__ == '__main__':
    print(sys.path)
    unittest.main()