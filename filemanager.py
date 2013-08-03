#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import string
from sqlite.operations import data
from string import Template
systemType = os.name

class fileManage:
    def __init__(self, fileName, fileSize):
        self.fileName = fileManage
        self.fileSize = fileSize
        self.status = ''

    def getFileStatus(self, fileName):
        sql = "select filelength from filedown where filename='%s'" % fileName
        length = data.selectOneResultOneCell(sql)
        if length == "":
            return 'false'
        else:
            return "".join(length)

    def __getFileList__(self, p, pagesize, curpage):
        p=str(p)
        if p=="":
            return []
        a = os.listdir(p)
        files=[]
        for x in a:
            if os.path.isfile(os.path.join(p,x)):
                file = fileManage(0,0)
                file.fileName = x
                file.fileSize = os.path.getsize(os.path.join(p,x))
                fileStatus = self.getFileStatus(x)
                if fileStatus != 'false':
                    if string.atoi(fileStatus) == file.fileSize or fileStatus == '':
                        file.status = '100'
                    else:
                        file.status = str((file.fileSize/string.atof(fileStatus))*100)
                else:
                    file.status = '100'
                files.append(file)
        curindex = pagesize*(curpage-1)
        i = 0
        arr=files[curindex:curindex+pagesize+1]
        dict = {'files': arr, 'total': len(files)}
        return dict

    @staticmethod
    def getFileList(p, pagesize, curpage):
        _data_ = fileManage(0, 0)
        return _data_.__getFileList__(p, pagesize, curpage)


