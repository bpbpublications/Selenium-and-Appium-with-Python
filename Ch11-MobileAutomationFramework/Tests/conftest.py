import pytest

from Base.Driver import Driver


@pytest.fixture(params=['Android'], scope="class")
def fixtureSetup(request):
    driver = None
    if request.param == "Android":
        driver = Driver().getAndroidDriverInstance()
        return driver
    elif request.param == "IOS":
        driver = Driver().getIOSDriverInstance()
        return driver
