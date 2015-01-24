# -*- coding: utf8 -*-
import urllib2
import string

serverIPList = ["172.0.0.1", "172.0.0.2", "172.0.0.3"]
failServerList = ""

for ip in serverIPList:
    f = urllib2.urlopen('http://%s' % ip)
    ntpcWebData = f.read()
    
    #判斷網頁AP是否正常
    checkData = "本系統多數補助對象為設籍新北市市民"
    if ntpcWebData.find(checkData) == -1:
        failServerList += "{0} AP Fail\n".format(ip)
    

if len(failServerList) != 0:
    #寄email通知管理者
    websiteAdmin = ["xxx@gmail.com","x"]
        
    import smtplib
    from email.mime.text import MIMEText
    
    msg = MIMEText(failServerList)
    msg['Subject'] = '[Monitor] Welfare Server AP Fail'
    msg['From'] = "aj1384@ms.ntpc.gov.tw"
    msg['To'] = ",".join(websiteAdmin)
    s = smtplib.SMTP('ms.ntpc.gov.tw')
    s.sendmail("@ntpc.gov.tw", websiteAdmin, msg.as_string())
    s.quit()
