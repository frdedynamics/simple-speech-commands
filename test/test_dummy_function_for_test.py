from unittest import TestCase
from .context import good_stuff


class TestDummyFunctionForTest(TestCase):
    def test_dummy_function_for_test(self):
        test_result = good_stuff.dummy_function_for_test()
        self.assertTrue(test_result)
        self.assertTrue(False)  # for fail test
