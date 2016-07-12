# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_login(self):
        success = True
        wd = self.wd
        wd.get("https://account.myparallels.com/")
        wd.find_element_by_xpath("//span[@id='main_container']//div[.=' ']").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("kpreis@parallels.com")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("123@qwE")
        wd.find_element_by_xpath("//form[@class='pax-form-narrow']//button[.='Sign In']").click()
        wd.find_element_by_xpath("//ul[@class='pax-sidenav__menu']//h3[.='Support']").click()
        wd.find_element_by_link_text("Parallels Desktop").click()
        wd.find_element_by_link_text("Parallels Access").click()
        wd.find_element_by_xpath("//ul[@class='pax-sidenav__menu']//h3[.='Parallels Desktop']").click()
        wd.find_element_by_link_text("Licenses").click()
        wd.find_element_by_link_text("Add").click()
        wd.find_element_by_css_selector("div.pax-sidenav-profile.pax-toggled").click()
        wd.find_element_by_css_selector("li.pax-sidenav-dropdown__link").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
