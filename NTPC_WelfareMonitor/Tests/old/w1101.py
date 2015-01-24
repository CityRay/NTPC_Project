#-*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class welfare01(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.11")
        self.selenium.start()
    
    def test_welfare01(self):
        sel = self.selenium
        sel.open("/welfare")
        sel.set_speed("800")
        sel.click("css=div.text-header3")
        sel.click("//div[@id='fbox1']/a")
        sel.wait_for_page_to_load("30000")
        sel.type("id=year-qsSS4globalglobal0", "66")
        sel.type("id=___cmbinput___month-qsSS4globalglobal0", "6")
        sel.type("name=day:qs%24SS4%24global%24global0", "6")
        sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
        sel.type("id=___cmbinput___qsSS4globalglobal2", u"低收入戶證明")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("css=ins.iCheck-helper")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=申請低收入戶資格-含改列、增列、減列及申覆")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=二節慰問金及三節加菜金")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=補助低收入戶及中低收入戶專用垃圾袋案")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
