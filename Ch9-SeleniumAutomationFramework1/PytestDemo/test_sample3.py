import pytest


@pytest.mark.usefixtures("fixtureSetup")
class Test_Sample3:

    @pytest.mark.fixtureDemo
    def test_fun5(self):
        print("\n" + "This is Function 5 in the Class Sample 3")

    @pytest.mark.fixtureDemo
    def test_fun6(self):
        print("\n" + "This is Function 6 in the Class Sample 3")
