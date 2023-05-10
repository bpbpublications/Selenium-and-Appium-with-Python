import pytest
import random


# @pytest.mark.xfail
def test_fun1Payment():
    print("\n" + "First Pytest Execution")


@pytest.mark.regression
def test_fun2():
    print("\n" + "Second Pytest Execution")


@pytest.mark.fixtureDemo
def test_fixtureDemo(fixtureSetup):
    print("\n" + "Pytest Demo Flow Execution")
    # assert isinstance(fixtureSetup, int)
    # assert 1 <= fixtureSetup <= 100
