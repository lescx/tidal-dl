#!/usr/bin/env python
from tidal_dl.lang.english import LangEnglish

class Language(object):
    def __init__(self) -> None:
        self.select = LangEnglish()

    def __toInt__(self, str):
        try:
            return int(str)
        except:
            return 1
    
    def setLang(self, index):
        index = self.__toInt__(index)
        self.select = LangEnglish()

LANG = Language()
