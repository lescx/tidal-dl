#!/usr/bin/env python

import sys
import getopt

from tidal_dl.events import *
from tidal_dl.settings import *

def mainCommand():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 
                                   "hvl:o:q:r:", 
                                   ["help", "version", "link=", "output=", "quality", "resolution"])
    except getopt.GetoptError as errmsg:
        Printf.err(vars(errmsg)['msg'] + ". Use 'tidal-dl -h' for usage.")
        return

    link = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            Printf.usage()
            return
        if opt in ('-v', '--version'):
            Printf.version()
            return
        if opt in ('-l', '--link'):
            link = val
            continue
        if opt in ('-o', '--output'):
            SETTINGS.downloadPath = val
            SETTINGS.save()
            continue
        if opt in ('-q', '--quality'):
            SETTINGS.audioQuality = SETTINGS.getAudioQuality(val)
            SETTINGS.save()
            continue
        if opt in ('-r', '--resolution'):
            SETTINGS.videoQuality = SETTINGS.getVideoQuality(val)
            SETTINGS.save()
            continue
    
    if not aigpy.path.mkdirs(SETTINGS.downloadPath):
        Printf.err(LANG.select.MSG_PATH_ERR + SETTINGS.downloadPath)
        return
    
    if link is not None:
        if not loginByConfig():
            loginByWeb()
        #Printf.info(LANG.select.SETTING_DOWNLOAD_PATH + ':' + SETTINGS.downloadPath)
        start(link)

def main():
    SETTINGS.read(getProfilePath())
    TOKEN.read(getTokenPath())
    TIDAL_API.apiKey = apiKey.getItem(SETTINGS.apiKeyIndex)
    
    if len(sys.argv) > 1:
        mainCommand()
        return
    
    if not apiKey.isItemValid(SETTINGS.apiKeyIndex):
        changeApiKey()
        loginByWeb()
    elif not loginByConfig():
        loginByWeb()
    
    while True:
        Printf.choices()
        choice = Printf.enter(LANG.select.PRINT_ENTER_CHOICE)
        if choice == "0":
            return
        elif choice == "1":
            if not loginByConfig():
                loginByWeb()
        elif choice == "2":
            loginByWeb()
        elif choice == "3":
            loginByAccessToken()
        elif choice == "4":
            if changeApiKey():
                loginByWeb()
        else:
            start(choice)

if __name__ == '__main__':
    main()
