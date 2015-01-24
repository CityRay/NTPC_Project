#-*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class welfare06(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.11")
        self.selenium.start()
    
    def test_welfare06(self):
        sel = self.selenium
        sel.open("/welfare")
        sel.set_speed("800")
        sel.click("//a[6]/div[2]/div[3]")
        sel.click("//div[@id='fbox2']/a")
        sel.wait_for_page_to_load("30000")
        sel.type("id=year-qsSS4globalglobal0", "60")
        sel.type("id=___cmbinput___month-qsSS4globalglobal0", "10")
        sel.type("name=day:qs%24SS4%24global%24global0", "22")
        sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
        sel.type("id=___cmbinput___qsSS4globalglobal2", u"一般身分")
        sel.click("//fieldset[@id='qsSS4globalglobal3']/span[2]/div/ins")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("//button[@type='button']")
        sel.type("id=___cmbinput___qsSSB1globalglobal0", u"去年度至三年內")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=整合式健康篩檢服務")
        sel.wait_for_page_to_load("30000")
        sel.click("id=opa104List")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click("id=reportattrglobal_text_policy113globalglobalRelevantfalsefalse")
        sel.wait_for_page_to_load("30000")
        sel.click("//ul[@id='drtree']/div/a[2]/img")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
