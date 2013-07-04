#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

import os
import bottle
import sqlite3
from sqlite import operations
from bottle import Bottle, run, template, static_file,request,response,route

app = Bottle()

host = "192.168.1.100"
port = 8080
url = "http://" + host + ":%d" % port

bottle.debug(True)

@app.route("/static/<filename:re:.*\.(css|js|png|jpg|ico|gif)>")
def static(filename):
    return static_file(filename, os.getcwd() + "/static/")


@app.get("/")
def index():
    return template("login")

@route('/login',method='POST')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    return template("download")


@app.error(404)
@app.error(405)
@app.error(500)
def error(error):
    return template("404", error=error)


run(app, host=host, port=port)
