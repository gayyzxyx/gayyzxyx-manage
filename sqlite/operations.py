__author__ = 'gayyzxyx'
import sqlite3
import os


class data:
    def __init__(self):
        self.db = "/mnt/wine/work/github/gayyzxyx-manage/db/bottle.db"
        self.connect = None
        self.cursor = None

    def __open__(self):
        self.connect = sqlite3.connect(self.db)
        self.cursor = self.connect.cursor()

    def __close__(self):
        self.cursor.close()
        self.connect.close()

    def __selectOneResultOneCell__(self, sql):
        self.__open__()
        self.cursor.execute(sql)
        turple = self.cursor.fetchall()
        if len(turple) >= 1:
            result = turple[0]
            self.__close__()
            return result
        else:
            self.__close__()
            return ""

    def __insertOneCell__(self, sql):
        self.__open__()
        self.cursor.execute(sql)
        self.connect.commit()
        self.__close__()

    @staticmethod
    def selectOneResultOneCell(sql):
        _data_ = data()
        return _data_.__selectOneResultOneCell__(sql)

    @staticmethod
    def insertOneCell(sql):
        _data_ = data()
        return _data_.__insertOneCell__(sql)
