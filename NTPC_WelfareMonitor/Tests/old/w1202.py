#-*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class welfare02(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.12")
        self.selenium.start()
    
    def test_welfare02(self):
        sel = self.selenium
        sel.open("/welfare")
        sel.set_speed("800")
        sel.click("//a[2]/div[2]/div")
        sel.click("//div[@id='fbox8']/a")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.type("id=year-qsSS4globalglobal0", "73")
        sel.type("id=___cmbinput___month-qsSS4globalglobal0", "6")
        sel.type("name=day:qs%24SS4%24global%24global0", "2")
        sel.type("id=___cmbinput___qsSS4globalglobal2", u"一般身分")
        sel.click("css=ins.iCheck-helper")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.type("id=qsSS8globalglobal0", "4")
        sel.type("id=qsSS8globalglobal1", "200000")
        sel.type("id=qsSS8globalglobal2", "200000")
        sel.type("id=qsSS8globalglobal3", "200000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("css=ins.iCheck-helper")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=辦理求職交通補助金")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click("id=reportattrglobal_text_policy100globalglobalRelevantfalsefalse")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
