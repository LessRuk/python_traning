# -*- coding: utf-8 -*-
import pytest,datetime
from fixture.application import Application

now_time = datetime.datetime.now()

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser,base_url=base_url)
    else:
        if not fixture.fixture_is_valid():
            fixture = Application(browser=browser,base_url=base_url)
    fixture.session.ensure_login(username="admin",password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")


