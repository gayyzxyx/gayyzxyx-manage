#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

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
        b = fileManage.getFileList("C:\\Windows\\",pagesize,curpage)
        return template("download",filelist=b['files'],total = b['total'],curpage = curpage)
    else:
        return template("login")

@app.route('/getfile/:index#[0-9]+#')
def getfiles(index):
    intIndex=string.atoi(index)
    b = fileManage.getFileList("C:\\Windows\\",pagesize,intIndex)
    return template("download",filelist=b['files'],total = b['total'],curpage = intIndex)
@app.error(404)
@app.error(405)
@app.error(500)
def error(error):
    return template("404", error=error)

run(app, host=host, port=port)





