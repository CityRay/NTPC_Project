# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from Tkinter import *
import io
import json
import urllib2


if __name__ == "__main__":

    root = Tk()
    root.geometry("600x260")
    root.title("get OpenData to CSV!")

    global_font=("Arial",16)

    label_Title = Label(root, font=global_font, text="Key URL:")
    label_Title.pack()
    filename_var=StringVar()
    entry=Entry(root, width=100, textvariable=filename_var)
    entry.pack()
    filename_var.set( "http://60.199.253.136/api/action/datastore_search?resource_id=d7a1b4c2-cad0-44f2-958a-a9d7a9330c95&limit=10000" )
    #print filename_var.get()

    label_Title2 = Label(root, font=global_font, text="\nKey filepath:")
    label_Title2.pack()    
    filename_var2=StringVar()
    entry2=Entry(root, width=100, textvariable=filename_var2)
    entry2.pack()
    filename_var2.set( "C:\TaipeiFree.csv" )
    #print filename_var2.get()    

    def click(event):  
        getdurl = entry.get()
        getdpath = entry2.get()
        
        #讀取資料
        url = r"{ourl}".format(ourl = getdurl)
        f = urllib2.urlopen(url)
        text = f.read()
        data = json.loads(text)["result"]["records"]

        output = r"{filepath}".format(filepath=getdpath)
        with io.open(output, "w+") as o:
            for item in json.loads(text)["result"]["records"]:
                tes = ("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(item["HOTSPOT_TYPE"],item["HOTSPOT_NAME"],item["AREA"],item["AP_ID"],item["ADDRESS"],item["LAT"],item["LNG"],item["_id"]))
                o.write(tes)

        #讀取資料結束
        label_Over = Label(root, font=global_font, text="\nParser OKOK!!!").pack()
        #print "GET OVER"
        
    btn = Button(root, text="SEND")
    btn.bind("<Button>",click)
    btn.pack(side = "bottom")
    
    root.mainloop()
