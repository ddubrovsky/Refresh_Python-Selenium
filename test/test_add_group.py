# -*- coding: utf-8 -*

from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="new_1", header="bla-bla-bla", footer="bla footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
