__author__ = 'Dmitrii'

from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        #self.return_to_home_page()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        # self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # click delete button
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/div[2]/input').click()
        # submit deletion
        wd.switch_to.alert.accept()

#   def return_to_home_page(self):
#       wd = self.app
#        if not (wd.current_url.endswith("/")) and len(wd.find_elements(By.LINK_TEXT, "Send e-Mail")) > 0:
#            wd.find_element(By.LINK_TEXT, "home page").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
