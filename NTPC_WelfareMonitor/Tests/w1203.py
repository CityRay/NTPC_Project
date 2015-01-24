#-*- coding: utf-8 -*-
from selenium import selenium
from datetime import datetime
import unittest, time, re

class welfare03(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.12")
        self.selenium.start()
    
    def test_welfare03(self):
        try:
            sel = self.selenium
            sel.window_maximize()
            sel.open("/welfare")
            sel.set_speed("600")
            sel.click("//a[3]/div[2]/div[3]")
            sel.click("//div[@id='fbox9']/a")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSS4globalglobal2", u"中低收入戶證明")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSSH1globalglobal0", u"1.家屬死亡卻無力殮葬。")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=申請急難救助")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click("id=reportattrglobal_text_policy27globalglobalRelevantfalsefalse")
            sel.wait_for_page_to_load("30000")
            sel.click("//ul[@id='drtree']/div/a[2]/img")
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
