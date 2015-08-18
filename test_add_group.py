# -*- coding: utf-8 -*-
import pytest,datetime
from group import Group
from application import Application

now_time = datetime.datetime.now()

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

########################################################################################################################
def test_test_add_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="123_" + str(now_time),header= "123_" + str(now_time),footer= "123"))
    app.logout()

def test_test_add_empty_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="",header= "",footer= ""))
    app.logout()

