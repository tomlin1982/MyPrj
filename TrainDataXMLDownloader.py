import os
import sys
import shutil
import urllib.request
import wget
from html.parser import HTMLParser
import time

from bs4 import BeautifulSoup



class XMLReader:

    def __init__(self, xml_url, DownLoadPath):
        self.xml_url = xml_url
        self.DownLoadPath = DownLoadPath

    def readdata(self):
        # print(url)
        self.response = urllib.request.urlopen(self.xml_url)
        self.data = self.response.read()      # a `bytes` object
        self.text = self.data.decode('utf-8')
        self.soup = BeautifulSoup(self.text, 'html.parser')

    def retrunfile_index(self):
        self.file_index = { }
        self.text_temp = []
        self.fileweblink_temp = []
        for link in self.soup.find_all('a'):
        # print(link.get('href'))
            self.fileweblink_temp.append("http://ods.railway.gov.tw/"+link.get('href'))
        
        for TextName in self.soup.find_all('tr'):
            self.text_temp.append(TextName.get_text().split( ))

        for i in range(1, len(self.text_temp)):
            self.file_index[self.text_temp[i][0]] = self.text_temp[len(self.text_temp)-i][3]

        return self.file_index

    def returnreverse_file_index(self):
        self.reverse_file_index = {value:key for key,value in self.file_index.items()}

        return self.reverse_file_index   
        
        
    def returnfiledownload_path(self):
        self.filedownload_path = { }
        k = int(len(self.fileweblink_temp))
        for i in range(0, len(self.fileweblink_temp)):
            self.filedownload_path[str(k-i)] = self.fileweblink_temp[i]
        return self.filedownload_path
    
    def currentDownLoadPath(self, mydownloadpath, myfilename, mybar):
        self.mydownloadpath = mydownloadpath
        self.myfilename = myfilename
        self.file_path = self.DownLoadPath+'\\'+self.myfilename

        wget.download(self.mydownloadpath, self.file_path, bar = mybar)
        return True
    

#範例測試
            
# folderpath = 'Downloads' #下載檔案的位置
# url = 'http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/railway_schedule/XML/list'

# mydata = XMLReader(url, folderpath)
# mydata.readdata()
# file_index_1 = mydata.retrunfile_index()
# reverse_file_index_1 = mydata.returnreverse_file_index()
# filedownload_path_index = mydata.returnfiledownload_path()

# print(file_index_1)
# print(reverse_file_index_1)
# print(filedownload_path_index)

# for mykey in file_index_1.keys():
#     print(file_index_1.get(mykey))
#     print(filedownload_path_index.get(mykey))
#     mydata.currentDownLoadPath(filedownload_path_index.get(mykey), file_index_1.get(mykey))


    



