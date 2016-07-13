# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")
    
    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, wd, group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, pwd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(pwd)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group("1q2w", "11", "22"))
        self.submit_group_creation(wd)
        self.return_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group("", "", ""))
        self.submit_group_creation(wd)
        self.return_group_page(wd)
        self.logout(wd)



    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
