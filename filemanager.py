#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
systemType = os.name

class fileManage:
    def __init__(self,fileName,fileSize):
        self.fileName = fileManage
        self.fileSize = fileSize

    def __getFileList__(self,p,pagesize,curpage):
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
                files.append(file)
        curindex = pagesize*(curpage-1)
        i = 0
        arr=files[curindex:curindex+pagesize+1]
        dict = {'files':arr,'total':len(files)}
        return dict
    @staticmethod
    def getFileList(p,pagesize,curpage):
        _data_ = fileManage(0,0)
        return _data_.__getFileList__(p,pagesize,curpage)
