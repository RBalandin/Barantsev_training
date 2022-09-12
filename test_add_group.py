# -*- coding: utf-8 -*-
from group import Group
from Application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_new_group(Group(name="asdfgh", header="asdfgh", footer="asdfgh"))
    app.return_to_groups()
    app.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_new_group(Group(name="", header="", footer=""))
    app.return_to_groups()
    app.logout()


if __name__ == "__main__":
    pytest.main()
