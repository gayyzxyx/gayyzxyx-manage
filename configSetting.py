#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.etree import ElementTree
class configSetting:
    def __init__(self):
        self.fileLocation = ""
        self.pagesize = 10
        self.tree = ElementTree.parse(r"FileLocation.xml")
        self.root = self.tree.getroot()

    def __readConfig__(self):
        self.fileLocation =  self.root.find('FileLocation').text
        self.pagesize = self.root.find("PageSize").text
        return {'fileLocation':self.fileLocation,'pagesize':self.pagesize}

    def __saveConfig__(self,data):
        fileLocation = data['fileLocation']
        self.root.find('FileLocation').text = fileLocation
        self.tree.write("FileLocation.xml")
        self.fileLocation = fileLocation
        return 1

    @staticmethod
    def readConfig():
        _config_ = configSetting()
        return _config_.__readConfig__()

    @staticmethod
    def saveConfig(data):
        _config_ = configSetting()
        return _config_.__saveConfig__(data)