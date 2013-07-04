__author__ = 'gayyzxyx'
import sqlite3
import os

db_path = "../db"
db_file = "bottle.db"
def initDb():
    if not os.path.exists(db_path):
        os.mkdir(db_path)

    if os.path.isfile("%s/%s" % (db_path, db_file)):
        print "[ERROR] DB FILE exists, could not be init DB."
        os.system("pause>nul")
        exit(0)
    else:
        connect = sqlite3.connect("%s/%s" % (db_path, db_file))
        cursor = connect.cursor()

        cursor.execute("""
            CREATE TABLE USER(
            ID INTEGER  PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(32) UNIQUE,
            PASSWORD  VARCHAR(32),
             PERMISSION INT
        )""")

def insert(name,password,permission):
    cx = sqlite3.connect("../db/bottle.db")
    cu = cx.cursor()
    cu.execute("insert into user(NAME,PASSWORD,PERMISSION) VALUES('%s','%s',%d)"%name,password,permission)
    cx.commit()

def getPassword(name):
    cx = sqlite3.connect("../db/bottle.db")
    cu = cx.cursor()
    cu.execute("SELECT PASSWORD,PERMISSION FROM USER WHERE NAME='%s'"%name)
    return cu.fetchone()
