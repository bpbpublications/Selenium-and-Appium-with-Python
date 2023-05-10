from time import sleep

import pytest
from softest import TestCase


class TestExample(TestCase):
    def test_addition(self):
        a = 2
        b = 2
        result = a + b
        self.soft_assert(self.assertEqual, result, 3)
        if result == 3:
            print("PASSED")
        else:
            print("FAILED")
        print("assert 3 Passed++++++++++++++++++")
        sleep(10)

        a = 3
        b = 3
        result = a + b
        self.soft_assert(self.assertEqual, result, 7)
        if result == 7:
            print("PASSED")
        else:
            print("FAILED")
        print("assert 4 Passed++++++++++++++++++++")
        sleep(10)

        self.assert_all()