#-*- coding: utf-8 -*-
from selenium import selenium
from datetime import datetime
import unittest, time, re

class welfare09(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.11")
        self.selenium.start()
    
    def test_welfare09(self):
        try:
            sel = self.selenium
            sel.window_maximize()
            sel.open("/welfare")
            sel.set_speed("600")
            sel.click("//a[9]/div[2]/div[2]")
            sel.click("//div[@id='fbox12']/a")
            sel.wait_for_page_to_load("30000")
            sel.type("id=year-qsSSQ2globalglobal0", "66")
            sel.type("id=___cmbinput___month-qsSSQ2globalglobal0", "6")
            sel.type("name=day:qs%24SSQ2%24global%24global0", "6")
            sel.type("id=___cmbinput___qsSSQ2globalglobal1", u"1.遭遇配偶死亡或是配偶失蹤未尋獲達六個月以上")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=qsSSQ3globalglobal0", "4")
            sel.type("id=qsSSQ3globalglobal1", "100000")
            sel.type("id=qsSSQ3globalglobal2", "100000")
            sel.type("id=qsSSQ3globalglobal3", "100000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=特殊境遇家庭")
            sel.wait_for_page_to_load("30000")
            sel.click("id=opa104List")
            sel.select("id=opa104List", u"label=萬里區公所")
            sel.click("css=option[value=\"116\"]")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=低收入戶")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=中低收入老人生活津貼")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=中低收入戶")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=中低收入兒童少年生活扶助")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click("css=img")
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
