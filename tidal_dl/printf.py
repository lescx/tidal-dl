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
        print(aigpy.cmd.red(LANG.select.PRINT_ERR + " ") + string)
        # logging.error(string)
        print_mutex.release()
        
    @staticmethod
    def info(string):
        global print_mutex
        print_mutex.acquire()
        print(aigpy.cmd.blue(LANG.select.PRINT_INFO + " ") + string)
        print_mutex.release()

    @staticmethod
    def success(string):
        global print_mutex
        print_mutex.acquire()
        print(aigpy.cmd.green(LANG.select.PRINT_SUCCESS + " ") + string)
        print_mutex.release()

    @staticmethod
    def album(data: Album):
        #tb = Printf.__gettable__([LANG.select.MODEL_ALBUM_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_TITLE, data.title],
        #    ["ID", data.id],
        #    [LANG.select.MODEL_TRACK_NUMBER, data.numberOfTracks],
        #    [LANG.select.MODEL_VIDEO_NUMBER, data.numberOfVideos],
        #    [LANG.select.MODEL_RELEASE_DATE, data.releaseDate],
        #    [LANG.select.MODEL_VERSION, data.version],
        #    [LANG.select.MODEL_EXPLICIT, data.explicit],
        #])
        print()
        #logging.info("====album " + str(data.id) + "====\n" +
        #             "title:" + data.title + "\n" +
        #             "track num:" + str(data.numberOfTracks) + "\n" +
        #             "video num:" + str(data.numberOfVideos) + "\n" +
        #             "==================================")

    @staticmethod
    def track(data: Track, stream: StreamUrl = None):
        #tb = Printf.__gettable__([LANG.select.MODEL_TRACK_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_TITLE, data.title],
        #    ["ID", data.id],
        #    [LANG.select.MODEL_ALBUM, data.album.title],
        #    [LANG.select.MODEL_VERSION, data.version],
        #    [LANG.select.MODEL_EXPLICIT, data.explicit],
        #    ["Max-Q", data.audioQuality],
        #])
        #if stream is not None:
        #    tb.add_row(["Get-Q", str(stream.soundQuality)])
        #    tb.add_row(["Get-Codec", str(stream.codec)])
        print()
        #logging.info("====track " + str(data.id) + "====\n" + \
        #             "title:" + data.title + "\n" + \
        #             "version:" + str(data.version) + "\n" + \
        #             "==================================")

    @staticmethod
    def video(data: Video, stream: VideoStreamUrl = None):
        #tb = Printf.__gettable__([LANG.select.MODEL_VIDEO_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_TITLE, data.title],
        #    [LANG.select.MODEL_ALBUM, data.album.title if data.album != None else None],
        #    [LANG.select.MODEL_VERSION, data.version],
        #    [LANG.select.MODEL_EXPLICIT, data.explicit],
        #    ["Max-Q", data.quality],
        #])
        #if stream is not None:
        #    tb.add_row(["Get-Q", str(stream.resolution)])
        #    tb.add_row(["Get-Codec", str(stream.codec)])
        print()
        #logging.info("====video " + str(data.id) + "====\n" +
        #             "title:" + data.title + "\n" +
        #             "version:" + str(data.version) + "\n" +
        #             "==================================")

    @staticmethod
    def artist(data: Artist, num):
        #tb = Printf.__gettable__([LANG.select.MODEL_ARTIST_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_ID, data.id],
        #    [LANG.select.MODEL_NAME, data.name],
        #    ["Number of albums", num],
        #    [LANG.select.MODEL_TYPE, str(data.type)],
        #])
        print()
        #logging.info("====artist " + str(data.id) + "====\n" +
        #             "name:" + data.name + "\n" +
        #             "album num:" + str(num) + "\n" +
        #             "==================================")

    @staticmethod
    def playlist(data):
        #tb = Printf.__gettable__([LANG.select.MODEL_PLAYLIST_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_TITLE, data.title],
        #    [LANG.select.MODEL_TRACK_NUMBER, data.numberOfTracks],
        #    [LANG.select.MODEL_VIDEO_NUMBER, data.numberOfVideos],
        #])
        print()
        #logging.info("====playlist " + str(data.uuid) + "====\n" +
        #             "title:" + data.title + "\n" +
        #             "track num:" + str(data.numberOfTracks) + "\n" +
        #             "video num:" + str(data.numberOfVideos) + "\n" +
        #             "==================================")

    @staticmethod
    def mix(data):
        #tb = Printf.__gettable__([LANG.select.MODEL_PLAYLIST_PROPERTY, LANG.select.VALUE], [
        #    [LANG.select.MODEL_ID, data.id],
        #    [LANG.select.MODEL_TRACK_NUMBER, len(data.tracks)],
        #    [LANG.select.MODEL_VIDEO_NUMBER, len(data.videos)],
        #])
        print()
        #logging.info("====Mix " + str(data.id) + "====\n" +
        #             "track num:" + str(len(data.tracks)) + "\n" +
        #             "video num:" + str(len(data.videos)) + "\n" +
        #             "==================================")

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
