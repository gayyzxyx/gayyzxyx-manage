#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import bottle
import sqlite3
import string
from sqlite.operations import  data
from bottle import Bottle, run, template, static_file,request,response
from string import Template
from filemanager import fileManage
app = Bottle()

host = "192.168.1.100"
port = 8080
url = "http://" + host + ":%d" % port
file_location = '../'
pagesize=10
curpage=1
bottle.debug(True)
fileLocation="H:\TDDOWNLOAD"

@app.route("/static/<filename:re:.*\.(css|js|png|jpg|ico|gif)>")
def static(filename):
    return static_file(filename, os.getcwd() + "/static/")


@app.get("/")
def index():
    return template("login")

@app.post('/login',method='POST')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    sql = "select password from user where name='%s'" % name
    s = Template(data.selectOneResultOneCell(sql))
    if(s.template == password):
        b = fileManage.getFileList(fileLocation,pagesize,curpage)
        return template("download",filelist=b['files'],total = b['total'],curpage = curpage)
    else:
        return template("login")

@app.route('/getfile/:index#[0-9]+#')
def getfiles(index):
    intIndex=string.atoi(index)
    b = fileManage.getFileList(fileLocation,pagesize,intIndex)
    return template("download",filelist=b['files'],total = b['total'],curpage = intIndex)

@app.post('/rename',method='POST')
def rename():
    #0表示成功 1表示文件不存在 2表示重命名失败
    newName = request.forms.get('newName')
    curPage = request.forms.get('curpage')
    oldName = request.forms.get('oldname')
    fileList = os.listdir(fileLocation)
    for file in fileList:
        if os.path.basename(file)==oldName:
            os.rename(file,newName)

    return "1"
@app.error(404)
@app.error(405)
@app.error(500)
def error(error):
    return template("404", error=error)

run(app, host=host, port=port)





