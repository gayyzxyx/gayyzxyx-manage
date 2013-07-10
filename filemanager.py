#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
systemType = os.name

class fileManage:
    def __getFileList__(self,p,pagesize,curpage):
        p=str(p)
        if p=="":
            return []
#        p=p.replace("/","\\")
#        if p[-1]!="\\":
#            p = p + "\\"
        a = os.listdir(p)
        files=[]
        for x in a:
            if os.path.isfile(os.path.join(p,x)):
                files.append(x)
        curindex = pagesize*(curpage-1)
        i = 0
        arr=files[curindex:curindex+pagesize+1]
        dict = {'files':arr,'total':len(files)}
        return dict
    @staticmethod
    def getFileList(p,pagesize,curpage):
        _data_ = fileManage()
        return _data_.__getFileList__(p,pagesize,curpage)
