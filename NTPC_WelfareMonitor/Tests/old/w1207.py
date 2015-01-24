#-*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class welfare07(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.12")
        self.selenium.start()
    
    def test_welfare07(self):
        sel = self.selenium
        sel.open("/welfare")
        sel.set_speed("800")
        sel.click("//a[7]/div[2]/div")
        sel.click("//div[@id='fbox7']/a")
        sel.wait_for_page_to_load("30000")
        sel.type("id=year-qsSS4globalglobal0", "55")
        sel.type("id=___cmbinput___month-qsSS4globalglobal0", "7")
        sel.type("name=day:qs%24SS4%24global%24global0", "10")
        sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
        sel.type("id=___cmbinput___qsSS4globalglobal2", u"一般身分")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.type("id=___cmbinput___qsSSF1globalglobal0", u"5 年以上")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click("css=ins.iCheck-helper")
        sel.click("//form[@id='owdInterviewForm']/div/table/tbody/tr[2]/td/div/span[2]/div/span/div/ins")
        sel.click("//form[@id='owdInterviewForm']/div/table/tbody/tr[3]/td/div/span[2]/div/span/div/ins")
        sel.click("//form[@id='owdInterviewForm']/div/table/tbody/tr[4]/td/div/span[2]/div/span/div/ins")
        sel.click("id=submit")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=都市更新整建維護經費補助")
        sel.wait_for_page_to_load("30000")
        sel.click("id=button")
        sel.wait_for_page_to_load("30000")
        sel.click("id=reportattrglobal_text_policy127globalglobalRelevantfalsefalse")
        sel.wait_for_page_to_load("30000")
        sel.click("//ul[@id='drtree']/div/a[2]/img")
        sel.wait_for_page_to_load("30000")
        sel.click("css=img")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
