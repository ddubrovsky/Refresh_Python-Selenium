# -*- coding: utf-8 -*

from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_1", header="bla-bla-bla", footer="bla footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
