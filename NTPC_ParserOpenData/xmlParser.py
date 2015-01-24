import logging
import sys
import urllib2
import xml.parsers.expat

if __name__ == "__main__":

   logging.basicConfig(format='%(asctime)s %(message)s', filename="logname.log", level=logging.DEBUG)
   
   name = "Activity.xml"
   filepath = "/getActivity/"
   
   try:
       # 讀取資料
       webFile = urllib2.urlopen('http://www.ntpc.gov.tw/Calendar.xml/')
       data = webFile.read()
       
       # 判斷伺服器是否有誤
       p = xml.parsers.expat.ParserCreate()
       p.Parse(data, 1)
       
       # 儲存檔案
       dataFile = open(filepath + name, "w+")
       dataFile.write(data)
       dataFile.close()
   except (urllib2.URLError, xml.parsers.expat.ExpatError, IOError) as error:
       logging.debug(str(error))
       sys.exit()
   except Exception as error:
       logging.debug(str(error))
       sys.exit()