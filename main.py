#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import bottle
from configSetting import configSetting
import string
from sqlite.operations import data
from bottle import Bottle, run, template, static_file, request, response
from string import Template
from filemanager import fileManage
import time, threading

app = Bottle()
host = "0.0.0.0"
port = 8080
url = "http://" + host + ":%d" % port
file_location = '../'
docConfig = configSetting.readConfig()
pagesize = string.atoi(docConfig['pagesize'])
fileLocation = docConfig['fileLocation']
curpage = 1
bottle.debug(True)
systemType = os.name


@app.route("/static/<filename:re:.*\.(css|js|png|jpg|ico|gif)>")
def static(filename):
    return static_file(filename, os.getcwd() + "/static/")


@app.get("/")
def index():
    return template("login")


@app.post('/login', method='POST')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if name == "" or password == "":
        return template("login")
    sql = "select password from user where name='%s'" % name
    docConfig = configSetting.readConfig()
    pagesize = string.atoi(docConfig['pagesize'])
    fileLocation = docConfig['fileLocation']
    s = data.selectOneResultOneCell(sql)
    if ("".join(s) == password):
        b = fileManage.getFileList(fileLocation, pagesize, curpage)
        return template("download", filelist=b['files'], total=b['total'], curpage=curpage, fileLocation=fileLocation)
    else:
        return template("login")


@app.route('/getfile/:index#[0-9]+#')
def getfiles(index):
    intIndex = string.atoi(index)
    docConfig = configSetting.readConfig()
    pagesize = string.atoi(docConfig['pagesize'])
    fileLocation = docConfig['fileLocation']
    b = fileManage.getFileList(fileLocation, pagesize, intIndex)
    return template("download", filelist=b['files'], total=b['total'], curpage=intIndex, fileLocation=fileLocation)


@app.post('/rename', method='POST')
def rename():
    #0表示成功 1表示文件不存在 2表示重命名失败
    newName = request.forms.get('newName')
    curPage = request.forms.get('curpage')
    oldName = request.forms.get('oldname')
    fileList = os.listdir(fileLocation)
    sql = "update filedown set filename='%s' where filename='%s'" % (newName, oldName)
    for file in fileList:
        if getCode(os.path.basename(file), 'gbk2utf') == oldName:
            try:
                os.rename(getCode(os.path.join(fileLocation, oldName), 'utf2gbk'),
                          getCode(os.path.join(fileLocation, newName), 'utf2gbk'))
                data.insertOneCell(sql)
                break
            except Exception, ex:
                return Exception, ":", ex
    return "1"


@app.post('/delete', method='POST')
def delete():
    docConfig = configSetting.readConfig()
    pagesize = string.atoi(docConfig['pagesize'])
    fileLocation = docConfig['fileLocation']
    filename = request.forms.get("filename")
    filedir = os.path.join(fileLocation, filename)
    sql = "delete from filedown where filename='%s'" % filename
    if os.path.isfile(getCode(filedir, 'utf2gbk')):
        try:
            data.insertOneCell(sql)
            os.remove(getCode(filedir, 'utf2gbk'))
            return "1"
        except Exception, ex:
            return Exception, ":", ex
    return "0"


@app.post('/download', method='POST')
def download():
    addr = request.forms.get('down_address')
    docConfig = configSetting.readConfig()
    pagesize = string.atoi(docConfig['pagesize'])
    fileLocation = docConfig['fileLocation']
    if addr != "":
        shellBash = "wget -c -P %s %s" % (fileLocation, addr)
        #        os.system(shellBash)
        runThread(shellBash)
    b = fileManage.getFileList(fileLocation, pagesize, curpage)
    return template("download", filelist=b['files'], total=b['total'], curpage=curpage, fileLocation=fileLocation)


@app.post('/saveConfig', method='POST')
def saveConfig():
    fileLocation = request.forms.get('fileLocation')
    cConfig = {'fileLocation': fileLocation}
    if configSetting.saveConfig(cConfig) == 1:
        return {'result': "true", 'newLocation': fileLocation}
    else:
        return "false"


def getCode(requestString, modal):
    if systemType == 'nt' and modal == 'gbk2utf':
        return requestString.decode("gbk").encode("utf-8")
    elif systemType == 'nt' and modal == 'utf2gbk':
        return requestString.decode("utf-8").encode("gbk")
    elif systemType == 'posix':
        return requestString


@app.error(404)
@app.error(405)
@app.error(500)
def error(error):
    return template("404", error=error)


class timer(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr
        self.thread_stop = False

    def run(self):
        shellLength = "curl -I %s | grep Content-Length|awk -F':' '{print $2}'" % self.addr
        fileLength = os.popen(shellLength, 'r').read().replace(' ','').replace('\r','').replace('\n', '')
        fileName = self.addr.split('/')[len(self.addr.split('/'))-1]
        if fileLength != '':
            sql = "insert into filedown(filename,filelength) values('%s','%s')" % (fileName, fileLength)
            data.insertOneCell(sql)
            os.system(self.addr)

    def stop(self):
        self.thread_stop = True

def runThread(addr):
    thread = timer(addr)
    thread.start()
    return


run(app, server="tornado", host=host, port=port)
#cherrypy.quickstart(app)




