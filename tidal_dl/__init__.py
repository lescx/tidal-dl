#!/usr/bin/env python

import sys
import getopt

from tidal_dl.events import *
from tidal_dl.settings import *

def main():
    # Read settings, token and API key
    SETTINGS.read(getProfilePath())
    TOKEN.read(getTokenPath())
    TIDAL_API.apiKey = apiKey.getItem(SETTINGS.apiKeyIndex)
    
    # User enters `tidal-dl [OPTIONS,LINK]`:
    # If user enters a flag or a URL then parse command line arguments;
    # otherwise check API key
    if len(sys.argv) > 1:
        handleCommandLineArgs()
        return
    
    # User enters `tidal-dl`:
    # If key is not valid, refresh and login and print current API key status
    if not apiKey.isItemValid(SETTINGS.apiKeyIndex):
        changeApiKey()
        loginByWeb()
    elif not loginByConfig():
        loginByWeb()


def handleCommandLineArgs():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 
           "hvql:",
           ["help", "version", "verbose", "quiet", "link="])
    except getopt.GetoptError as errmsg:
        Printf.err(vars(errmsg)['msg'] + ". Use 'tidal-dl -h' for usage.")
        return

    link = None
    for opt, val in opts:
        if opt in ('-h', '--help'):
            Printf.help()
            return
        if opt in ('--version'):
            Printf.version()
            return
        if opt in ('-v', '--verbose'):
            print("-v, --verbose placeholder")
            continue
        if opt in ('-q', '--quiet'):
            print("-q, --quiet placeholder")
            continue
        if opt in ('-l', '--link'):
            link = val
            continue
    
    # Create download path if not exist
    if not aigpy.path.mkdirs(SETTINGS.downloadPath):
        Printf.err(LANG.select.MSG_PATH_ERR + SETTINGS.downloadPath)
        return
    
    # If user provided a link, try log in and then start.
    if link is not None:
        if not loginByConfig():
            loginByWeb()
        start(link)


if __name__ == '__main__':
    main()
