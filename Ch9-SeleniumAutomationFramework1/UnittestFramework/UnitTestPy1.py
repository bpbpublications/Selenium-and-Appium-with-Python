import unittest


class UnitDemo(unittest.TestCase):

    def setUp(self) -> None:
        print("This is setup")

    def test_function(self):
        print("This is the test")

    def tearDown(self) -> None:
        print("This is teardown")


if __name__ == "__main__":
    UnitDemo.test_function()
