#!/usr/bin/python
#-*- coding: utf-8 -*-
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile()
#print dir(drive.CreateFile())
file1.SetContentFile('p.png')
file1.Upload()
#print dir(file1.Upload())

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print 'title: %s, id: %s' % (file1['title'], file1['id'])

#print 'Created file %s with mimeType %s' % (file1['title'], file1['mimeType'])
