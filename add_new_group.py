# -*- coding: utf-8 -*

import unittest
from application import Application
from group import Group

class AddNewGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_new_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="new_1", header="bla-bla-bla", footer="bla footer"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
