__author__ = 'gayyzxyx'
import sqlite3
import os



class data:
    def __init__(self):
        self.db = "../db/bottle.db"
        self.connect = None
        self.cursor = None
    def __open__(self):
        self.connect = sqlite3.connect(self.db)
        self.cursor = self.connect.cursor()

    def __close__(self):
        self.cursor.close()
        self.connect.close()

    def __selectOneResultOneCell__(self,sql):
        self.__open__()
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        self.__close__()
        return result
    @staticmethod
    def selectOneResultOneCell(sql):
        _data_ = data()
        return _data_.__selectOneResultOneCell__(sql)
