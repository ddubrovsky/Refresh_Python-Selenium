__author__ = 'Dmitrii'

from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_groups = app.group.get_group_list()
    app.contact.delete_first_contact()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)