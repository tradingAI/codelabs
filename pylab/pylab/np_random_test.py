import unittest

import numpy as np

from pylab.np_random import get_random


class TestNumpyRandom(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        np.random.seed(seed=0)

    def test_get_random(self):
        self.assertEqual(0.5488135039273248, get_random())


if __name__ == '__main__':
    unittest.main()
