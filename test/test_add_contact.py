__author__ = 'Dmitrii'

from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Demetra", lastname="Fly", mobile="+123-456-7890", email="some@gmail.com"))
    app.session.logout()
