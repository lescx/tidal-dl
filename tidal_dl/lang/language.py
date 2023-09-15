#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   language.py
@Time    :   2023/09/15
@Author  :   les.cx
@Version :   0.1
@Contact :   luca@les.cx
@Desc    :   
'''

from tidal_dl.lang.english import LangEnglish

_ALL_LANGUAGE_ = [
    ['English', LangEnglish()],
]

class Language(object):
    def __init__(self) -> None:
        self.select = LangEnglish()

    def __toInt__(self, str):
        try:
            return int(str)
        except:
            return 0
    
    def setLang(self, index):
        index = self.__toInt__(index)
        if index >= 0 and index < len(_ALL_LANGUAGE_):
            self.select = _ALL_LANGUAGE_[index][1]
        else:
            self.select = LangEnglish()

    def getLangName(self, index):
        index = self.__toInt__(index)
        if index >= 0 and index < len(_ALL_LANGUAGE_):
            return _ALL_LANGUAGE_[index][0]
        return ""

    def getLangChoicePrint(self):
        array = []
        index = 0
        while True:
            name = self.getLangName(index)
            if name == "":
                break
            array.append('\'' + str(index) + '\'-' + name)
            index += 1
        return ','.join(array)


LANG = Language()
