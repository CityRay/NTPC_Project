#-*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class welfare05(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.12")
        self.selenium.start()
    
    def test_welfare05(self):
        sel = self.selenium
        sel.open("/welfare")
        sel.set_speed("800")
        sel.click("//a[5]/div[2]/div[2]")
        sel.click("//div[@id='fbox3']/a")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.type("id=year-qsSS4globalglobal0", "50")
        sel.type("id=___cmbinput___month-qsSS4globalglobal0", "2")
        sel.type("name=day:qs%24SS4%24global%24global0", "2")
        sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
        sel.type("id=___cmbinput___qsSS4globalglobal2", u"一般身分")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=生育獎勵金")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=孕婦乙型鏈球菌篩檢")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
