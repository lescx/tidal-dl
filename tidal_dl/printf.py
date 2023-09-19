#!/usr/bin/env python

from pickle import GLOBAL
import threading
import aigpy
import logging

import tidal_dl.apiKey as apiKey

from tidal_dl.model import *
from tidal_dl.paths import *
from tidal_dl.settings import *
from tidal_dl.lang.language import *


version = 'v0.1.0'
print_mutex = threading.Lock()


class Printf(object):

    @staticmethod
    def version():
        print(version)

    @staticmethod
    def help():
        print("""    -h, --help          show help-message
    -v, --version         show version
    -l, --link            URL/ID/filePath""")
        
    @staticmethod
    def enter(string):
        print(string)
        ret = input("")
        return ret
    
    @staticmethod
    def enterBool(string):
        print(string)
        ret = input("")
        return ret == '1'

    @staticmethod
    def enterPath(string, errmsg, retWord='0', default=""):
        while True:
            ret = aigpy.cmd.inputPath(string, retWord)
            if ret == retWord:
                return default
            elif ret == "":
                print(LANG.select.PRINT_ERR + " " + errmsg)
            else:
                break
        return ret

    @staticmethod
    def enterLimit(string, errmsg, limit=[]):
        while True:
            ret = aigpy.cmd.inputLimit(string, limit)
            if ret is None:
                print(LANG.select.PRINT_ERR + " " + errmsg)
            else:
                break
        return ret

    @staticmethod
    def enterFormat(string, current, default):
        ret = Printf.enter(string)
        if ret == '0' or aigpy.string.isNull(ret):
            return current
        if ret.lower() == 'default':
            return default
        return ret

    @staticmethod
    def err(string):
        global print_mutex
        print_mutex.acquire()
        print(LANG.select.PRINT_ERR + " " + string)
        # logging.error(string)
        print_mutex.release()
        
    @staticmethod
    def info(string):
        global print_mutex
        print_mutex.acquire()
        print(LANG.select.PRINT_INFO + " " + string)
        print_mutex.release()

    @staticmethod
    def success(string):
        global print_mutex
        print_mutex.acquire()
        print(LANG.select.PRINT_SUCCESS + " " + string)
        print_mutex.release()

    @staticmethod
    def album(data: Album):
        print("Downloading album:" + data.title + '…\n')
        
    @staticmethod
    def track(data: Track, stream: StreamUrl = None):
        print("Downloading track:" + data.title + '…\n')
        
    @staticmethod
    def video(data: Video, stream: VideoStreamUrl = None):
        print("Downloading video:" + data.title + '…\n')

    @staticmethod
    def artist(data: Artist, num):
        print("Downloading artist:" + data.title + '…\n')

    @staticmethod
    def playlist(data):
        print("Downloading playlist:" + data.title + '…\n')

    @staticmethod
    def mix(data):
        print("Downloading mix:" + data.id + '…\n')

    @staticmethod
    def apikeys(items):
        #print("API-Keys")
        #tb = prettytable.PrettyTable()
        #tb.field_names = [aigpy.cmd.green('Index'), 
        #                  aigpy.cmd.green('Valid'),
        #                  aigpy.cmd.green('Platform'), 
        #                  aigpy.cmd.green('Formats'), ]
        #tb.align = 'l'
        #
        #for index, item in enumerate(items):
        #    tb.add_row([str(index), 
        #                aigpy.cmd.green('True') if item["valid"] == "True" else aigpy.cmd.red('False'),
        #                item["platform"], 
        #                item["formats"]])
        print("wip apikeys()")
