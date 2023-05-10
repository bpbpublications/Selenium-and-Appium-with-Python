from time import sleep

import pytest
from softest import TestCase


class TestExample2(TestCase):
    def test_addition2(self):
        a = 2
        b = 2
        result = a + b
        self.soft_assert(self.assertEqual, result, 5)
        if result == 5:
            print("PASSED")
        else:
            print("FAILED")
        print("assert 1 Passed++++++++++++++++++")
        sleep(10)

        a = 3
        b = 3
        result = a + b
        self.soft_assert(self.assertEqual, result, 7)
        if result == 7:
            print("PASSED")
        else:
            print("FAILED")
        print("assert 2 Passed++++++++++++++++++++")
        sleep(10)

        self.assert_all()

