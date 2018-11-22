from unittest import TestCase
from heihei import dummy_function_for_test


class TestDummyFunctionForTest(TestCase):
    def test_dummy_function_for_test(self):
        test_result = dummy_function_for_test()
        self.assertTrue(test_result)
