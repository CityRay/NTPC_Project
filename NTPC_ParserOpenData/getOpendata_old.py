# -*- coding: UTF-8 -*-
from __future__ import division
import io
import json
import math
import re
import urllib2

def getNumOfRecord(dataUrl):
    f = urllib2.urlopen(dataUrl)
    str = f.read()
    str = str.split("紀錄筆數：")[1]
    str = str.split("參考網址：")[0]
    m = re.search(r"\d+", str)
    
    return int(m.group(0))

def getData(numOfRecord, dataId, maxRetrieveNum):
    #存放所有json物件
    totalData = []
    
    #讀取資料
    for i in range(0,(int)(math.ceil(numOfRecord / maxRetrieveNum))):
        url = "http://data.ntpc.gov.tw/NTPC/od/data/api/{dataId}/?$format=json&$top={maxRetrieveNum}&$skip={skip}".format(dataId = dataId, maxRetrieveNum = maxRetrieveNum, skip = (i*maxRetrieveNum))
        f = urllib2.urlopen(url)
        str = f.read()
        for item in json.loads(str):
            totalData.append(item)
    #print len(totalData) 
    return json.dumps(totalData, ensure_ascii = False) 

if __name__ == "__main__":
    try:
        #讀取Google管理資料
        url = "data.json"
        data = urllib2.urlopen(url)
        str = data.read().decode("utf-8")
        opendata = json.loads(str)
        data.close()
        #j = json.dumps(opendata, encoding="utf-8")
        #curl = opendata[u'feed'][u'entry'][0][u'gsx$opendatasite'][u'$t']
        #opendataid = opendata[u'feed'][u'entry'][0][u'gsx$opendataid'][u'$t']
        #dname = opendata[u'feed'][u'entry'][0][u'gsx$type'][u'$t']
        #filename = opendata[u'feed'][u'entry'][0][u'gsx$fileid'][u'$t']
        #print opendata

        i = 0
        for item in opendata[u'feed'][u'entry']:
            curl = opendata[u'feed'][u'entry'][i][u'gsx$opendatasite'][u'$t']
            opendataid = opendata[u'feed'][u'entry'][i][u'gsx$opendataid'][u'$t']
            dname = opendata[u'feed'][u'entry'][i][u'gsx$type'][u'$t']
            filename = opendata[u'feed'][u'entry'][i][u'gsx$fileid'][u'$t']
            #print i
            #print curl
            #print opendataid
            #print dname
            #print filename
            #print ' '

            try:
                #資料筆數所在網頁
                dataUrl = curl
                numOfRecord = getNumOfRecord(dataUrl)
                
                #擷取資料
                dataId = opendataid
                maxRetrieveNum = 1000
                text = getData(numOfRecord, dataId, maxRetrieveNum)
                
                #過濾資料
                if filename == "wifi":
                    text = text.replace("[iTaiwan]", "")
                    text = text.replace("[TPE-Free]", "")
                    #print "textReplace"
                
                #輸出檔案
                #output = "C:\\python_tmp\\" + dname + "\\" + filename + ".json"
                output = "/home/sites/ntpc/data/" + dname + "/" + filename + ".json"
                with io.open(output, "w+", encoding = 'utf-8') as f:
                    f.write(text)
            except IOError as IOE :
                print 'fault' + IOE.message
            except Exception:
                pass
            
            i += 1
    except Exception:
        pass
