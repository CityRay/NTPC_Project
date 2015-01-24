#-*- coding: utf-8 -*-
from selenium import selenium
from datetime import datetime
import unittest, time, re

class welfare04(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.11")
        self.selenium.start()
    
    def test_welfare04(self):
        try:
            sel = self.selenium
            sel.window_maximize()
            sel.open("/welfare")
            sel.set_speed("600")
            sel.click("//a[4]/div[2]/div[2]")
            sel.click("id=fbox5")
            sel.click("//div[@id='fbox5']/a")
            sel.wait_for_page_to_load("30000")
            sel.type("id=year-qsSS4globalglobal0", "30")
            sel.type("id=___cmbinput___month-qsSS4globalglobal0", "2")
            sel.type("name=day:qs%24SS4%24global%24global0", "1")
            sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
            sel.type("id=___cmbinput___qsSS4globalglobal2", u"中低收入戶證明")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("css=ins.iCheck-helper")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("//button[@type='button']")
            sel.type("id=___cmbinput___qsSS6globalglobal1", u"中度")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=長期照顧服務-緊急救援服務")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=獨居老人關懷服務")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=建立社區照顧關懷據點")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
        except Exception as e:
            print "============================ERROR================================="
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            png = self.selenium.capture_screenshot_to_string()
            f = open('/home/selenium/log/error-%s.png' % now, 'wb')
            f.write(png.decode('base64'))
            f.close()
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
