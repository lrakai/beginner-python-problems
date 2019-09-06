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
        self.assertEqual(odds(['This', 'one', 'is', 'hidden', '.']), 
                              ['one', 'hidden'])

    def test_challenge_two(self):
        # tests are specific to system created by cloudformation
        self.assertEqual(traversal_count('/opt/yarn/bin/'), 5)
        self.assertEqual(traversal_count('/usr/share/X11/'), 191)
        self.assertEqual(traversal_count('/usr/include/X11/', 97))


if __name__ == '__main__':
    unittest.main()
