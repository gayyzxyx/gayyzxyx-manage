#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

import os
import bottle
import sqlite3
from sqlite.operations import  data
from bottle import Bottle, run, template, static_file,request,response
from string import Template
from filemanager import fileManage
app = Bottle()

host = "192.168.1.100"
port = 8080
url = "http://" + host + ":%d" % port
file_location = '../'
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
        b = fileManage.getFileList("C:\\")
        return template("download")
    else:
        return template("login")


@app.error(404)
@app.error(405)
@app.error(500)
def error(error):
    return template("404", error=error)

run(app, host=host, port=port)





