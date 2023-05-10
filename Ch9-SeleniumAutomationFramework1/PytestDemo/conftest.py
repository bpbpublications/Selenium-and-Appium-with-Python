import pytest


@pytest.fixture(scope="class")
def fixtureSetup():
    print("\n" + "Pytest Fixture to Setup")
    # return random.randint(1, 100)
    yield
    print("\n" + "Pytest Fixture to TearDown")


@pytest.fixture(params=[("username1", "password1"), ("username2", "password2"), ("username3","password3")])
def loginfixture(request):
    return request.param
