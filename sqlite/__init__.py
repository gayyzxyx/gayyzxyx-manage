__author__ = 'gayyzxyx'
import os
import sqlite3

#db_path = "../db"
#db_file = "bottle.db"
#
#if not os.path.exists(db_path):
#    os.mkdir(db_path)
#
#if os.path.isfile("%s/%s" % (db_path, db_file)):
#    print "[ERROR] DB FILE exists, could not be init DB."
#    os.system("pause>nul")
#    exit(0)
#connect = sqlite3.connect("%s/%s" % (db_path, db_file))
#cursor = connect.cursor()
#
#cursor.execute("""
#        CREATE TABLE USER(
#        ID INTEGER  PRIMARY KEY AUTOINCREMENT,
#        NAME VARCHAR(32) UNIQUE,
#        PASSWORD  VARCHAR(32),
#        PERMISSION INT
#)""")
#
#cursor.execute("insert into user (NAME,PASSWORD,PERMISSION) VALUES('yaoxin','19900416',1)")
#connect.commit()
#cursor.close()
#connect.close()

