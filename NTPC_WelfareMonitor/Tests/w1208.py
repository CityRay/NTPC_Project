#-*- coding: utf-8 -*-
from selenium import selenium
from datetime import datetime
import unittest, time, re

class welfare08(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://172.18.124.12")
        self.selenium.start()
    
    def test_welfare08(self):
        try:
            sel = self.selenium
            sel.window_maximize()
            sel.open("/welfare")
            sel.set_speed("600")
            sel.click("//a[8]/div[2]/div[2]")
            sel.click("//div[@id='fbox6']/a")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSS3globalglobal1", u"教育相關")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=year-qsSS4globalglobal0", "88")
            sel.type("id=___cmbinput___month-qsSS4globalglobal0", "7")
            sel.type("name=day:qs%24SS4%24global%24global0", "7")
            sel.type("id=___cmbinput___qsSS4globalglobal1", u"約12個月以上")
            sel.type("id=___cmbinput___qsSS4globalglobal2", u"低收入戶證明")
            sel.click("//form[@id='owdInterviewForm']/div/table/tbody/tr[5]/td/div/span[2]/div/span/div/ins")
            sel.click("//form[@id='owdInterviewForm']/div/table/tbody/tr[6]/td/div/span[2]/div/span/div/ins")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSS5globalglobal0", u"高中")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSS6globalglobal0", u"輕度 - 持有身心障礙證明(手冊)")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=qsSS8globalglobal1", "10000")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.type("id=___cmbinput___qsSSE1globalglobal0", u"軍人半公費")
            sel.click("id=submit")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=身心障礙學生及身心障礙人士子女就學費用減免")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=體育獎學金申請撥付")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=高級中等以下學校辦理軍公教遺族就學費用優待")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=辦理市立高中職暨國民中小學學生午餐補助")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=申請低收入戶就學生活補助")
            sel.wait_for_page_to_load("30000")
            sel.click("id=button")
            sel.wait_for_page_to_load("30000")
            sel.click(u"link=教科書補助")
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
