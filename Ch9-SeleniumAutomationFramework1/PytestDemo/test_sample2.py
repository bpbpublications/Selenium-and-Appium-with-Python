import pytest


@pytest.mark.regression
def test_fun3Payment():
    print("\n" + "Third Pytest Execution")
    assert 1 == 1, "One is not equal to Two"


@pytest.mark.smoke
def test_fun4Shipping():
    print("\n" + "Fourth Pytest Execution")
    assert 1 == 1, "One is not equal to Two"
