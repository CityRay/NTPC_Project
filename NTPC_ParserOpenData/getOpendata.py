# -*- coding: UTF-8 -*-
from __future__ import division
from __future__ import unicode_literals
import io
import json
import logging
import math
import re
import time
import urllib2
import urllib
import xml.parsers.expat

def getNumOfRecord(dataUrl):
    while True:
        try:
            f = urllib2.urlopen(dataUrl)
            webHtml = f.read().decode("utf-8")
            webHtml = webHtml.split("紀錄筆數：")[1]
            webHtml = webHtml.split("參考網址：")[0]
            m = re.search(r"\d+", webHtml)
            f.close()
            break
        except Exception as e:
            logging.debug("In getNumOfRecord: " + str(e).decode('utf-8'))
            time.sleep(60)
            continue
            
    return int(m.group(0))

def getData(numOfRecord, dataId, area, gps):
    maxRetrieveNum = 2000
    
    #存放所有json物件
    totalData = []

    #讀取資料
    for i in range(0, (int)(math.ceil(numOfRecord / maxRetrieveNum))):
        while True:
            try:
                url = "http://data.ntpc.gov.tw/NTPC/od/data/api/{dataId}/?$format=json&$top={maxRetrieveNum}&$skip={skip}".format(dataId = dataId, maxRetrieveNum = maxRetrieveNum, skip = (i* maxRetrieveNum))
                f = urllib2.urlopen(url)
                for item in json.loads(f.read()):
                    totalData.append(item)
                f.close()
                break
            except Exception as e:
                logging.debug("In getData: " + str(e).decode('utf-8'))
                time.sleep(60)
                continue
    
    #加區域
    #if area != "done":
    for i in xrange(len(totalData)):
        #加區域
        if area != "done":    
            totalData[i]["area"] = getAreaFromAddress(totalData[i][area])

        #加座標
        if gps != "done":
            if gps.startswith("$"):
                totalData[i]["Px"],totalData[i]["Py"] = totalData[i][gps[1:]].split(",")
            else:
                totalData[i]["Px"],totalData[i]["Py"] = getLatLngFromAddress(totalData[i][gps])
    
    return json.dumps(totalData, ensure_ascii = False)

def getAreaFromAddress(address):    
    zipCode = ["板橋區","中和區","新莊區","三重區","新店區","土城區","永和區","蘆洲區","汐止區","樹林區","淡水區","三峽區","林口區","鶯歌區","五股區","泰山區","瑞芳區","八里區","深坑區","三芝區","萬里區","金山區","貢寮區","石門區","雙溪區","石碇區","坪林區","烏來區","平溪區"]
    for code in zipCode:
        if address.find(code) != -1:
            return code

def getLatLngFromAddress(address):
    while True:
        try:
            mapAPI = "http://data.ntpc.gov.tw/NTPC/gis/addrXY/json?addr=" + urllib.quote(address.encode("utf-8"))
            f = urllib2.urlopen(mapAPI)
            mapData = json.loads(f.read())
            f.close()
            time.sleep(0.4)
            break;
        except Exception as e :
            logging.debug("In getLatLngFromAddress: " + str(e).decode('utf-8'))
            time.sleep(60)
            continue
    
    return mapData["wgs84aX"], mapData["wgs84aY"]

def getNTPC(nURL, nfile):
    try:
       # 讀取資料
       webFile = urllib2.urlopen(nURL)
       data = webFile.read()
       
       # 判斷檔案是否有誤
       p = xml.parsers.expat.ParserCreate()
       p.Parse(data, 1)
       
       webFile.close()
       return data
    except Exception as error:
       logging.debug("In 讀取 " + nfile + " 市府官網資料: " + str(error).decode('utf-8'))
       return False    

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename="/home/kurogo/ntpc/cron/log/getOpendata.log", level=logging.DEBUG)

    logging.debug("開始讀取Google管理資料")
    #讀取Google管理資料
    opendata = ""
    while True:
        try:
            url = "https://spreadsheets.google.com/feeds/list/0AmL36SR2y5BwdDJaeFFSMHR2M1QxNE1jZHo5QzNPaFE/od6/public/values?alt=json"
            f = urllib2.urlopen(url)
            opendata = json.loads(f.read())
            f.close()
            break
        except Exception as e:
            logging.debug("In 讀取Google管理資料: " + str(e).decode('utf-8'))
            time.sleep(60)
            continue
    logging.debug("結束讀取Google管理資料")

    for item in opendata["feed"]["entry"]:
        dataUrl = item["gsx$opendatasite"]["$t"]
        opendataid = item["gsx$opendataid"]["$t"]
        dname = item["gsx$type"]["$t"]
        filename = item["gsx$fileid"]["$t"]
        source = item["gsx$source"]["$t"]
        area = item["gsx$area"]["$t"]
        gps = item["gsx$gps"]["$t"]
        
        if source == "OD":
            #擷取資料總筆數
            logging.debug("開始讀取OD: " + filename + "資料筆數")
            numOfRecord = getNumOfRecord(dataUrl)
            logging.debug("結束讀取OD: " + filename + "資料筆數")
            
            #擷取資料
            logging.debug("開始擷取OD: " + filename + "資料")
            text = getData(numOfRecord, opendataid, area, gps)
            logging.debug("結束擷取OD: " + filename + "資料")
            
            #過濾資料
            if filename == "wifi":
                text = text.replace("[iTaiwan]", "")
                text = text.replace("[TPE-Free]", "")

            #輸出檔案
            logging.debug("開始輸出OD: " + filename + "檔案")
            output = "/home/kurogo/ntpc/sites/ntpc/data/" + dname + "/" + filename + ".json"            
            with io.open(output, "w+", encoding = 'utf-8') as f:
                f.write(text)
            logging.debug("結束擷取OD: " + filename + "檔案")           
            #print "OPENDATA"

        elif source =="NTPC":
            logging.debug("開始擷取NTPC: " + filename + "資料")
            text = getNTPC(dataUrl, filename)
            #print type(text)
            logging.debug("結束擷取NTPC: " + filename + "資料")

            if text != False:
                logging.debug("開始輸出NTPC: " + filename + "檔案")
                output = "/home/kurogo/ntpc/sites/ntpc/data/" + dname + "/" + filename + ".xml"                
                with io.open(output, "w+", encoding = 'utf-8') as f:
                    f.write(text.decode('utf-8'))
                logging.debug("結束擷取NTPC: " + filename + "檔案")
            #print "NTPC"