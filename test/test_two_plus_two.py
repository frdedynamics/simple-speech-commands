from unittest import TestCase
from .context import good_stuff


class TestTwoPlusTwo(TestCase):
    def test_two_plus_two(self):
        test_result = good_stuff.two_plus_two()
        self.assertEqual(4, test_result, msg="two plus two is what? test result was: " + str(test_result))
