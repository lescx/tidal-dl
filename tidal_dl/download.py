#!/usr/bin/env python

import aigpy
import logging

from tidal_dl.paths import *
from tidal_dl.printf import *
from tidal_dl.decryption import *
from tidal_dl.tidal import *

from concurrent.futures import ThreadPoolExecutor

def __isSkip__(finalpath, url):
    if not SETTINGS.checkExist:
        return False
    curSize = aigpy.file.getSize(finalpath)
    if curSize <= 0:
        return False
    netSize = aigpy.net.getSize(url)
    return curSize >= netSize


def __encrypted__(stream, srcPath, descPath):
    if aigpy.string.isNull(stream.encryptionKey):
        os.replace(srcPath, descPath)
    else:
        key, nonce = decrypt_security_token(stream.encryptionKey)
        decrypt_file(srcPath, descPath, key, nonce)
        os.remove(srcPath)


def __parseContributors__(roleType, Contributors):
    if Contributors is None:
        return None
    try:
        ret = []
        for item in Contributors['items']:
            if item['role'] == roleType:
                ret.append(item['name'])
        return ret
    except:
        return None


def __setMetaData__(track: Track, album: Album, filepath, contributors, lyrics):
    obj = aigpy.tag.TagTool(filepath)
    obj.album = track.album.title
    obj.title = track.title
    if not aigpy.string.isNull(track.version):
        obj.title += ' (' + track.version + ')'

    obj.artist = list(map(lambda artist: artist.name, track.artists))
    obj.copyright = track.copyRight
    obj.tracknumber = track.trackNumber
    obj.discnumber = track.volumeNumber
    obj.composer = __parseContributors__('Composer', contributors)
    obj.isrc = track.isrc

    obj.albumartist = list(map(lambda artist: artist.name, album.artists))
    obj.date = album.releaseDate
    obj.totaldisc = album.numberOfVolumes
    obj.lyrics = lyrics
    if obj.totaldisc <= 1:
        obj.totaltrack = album.numberOfTracks
    coverpath = TIDAL_API.getCoverUrl(album.cover, "1280", "1280")
    obj.save(coverpath)


def downloadCover(album):
    if album is None:
        return
    path = getAlbumPath(album) + '/cover.jpg'
    url = TIDAL_API.getCoverUrl(album.cover, "1280", "1280")
    aigpy.net.downloadFile(url, path)


def downloadAlbumInfo(album, tracks):
    if album is None:
        return

    path = getAlbumPath(album)
    aigpy.path.mkdirs(path)

    path += '/albumInfo.txt'
    infos = ""
    infos += "ID          %s\n" % (str(album.id))
    infos += "Title       %s\n" % (str(album.title))
    infos += "Artists     %s\n" % (TIDAL_API.getArtistsName(album.artists))
    infos += "ReleaseDate %s\n" % (str(album.releaseDate))
    infos += "SongNum     %s\n" % (str(album.numberOfTracks))
    infos += "Duration    %s\n" % (str(album.duration))
    infos += '\n'

    for index in range(0, album.numberOfVolumes):
        volumeNumber = index + 1
        infos += f"CD {volumeNumber}\n"
        for item in tracks:
            if item.volumeNumber != volumeNumber:
                continue
            infos += '{:<8}'.format("%d" % item.trackNumber)
            infos += "%s\n" % item.title
    aigpy.file.write(path, infos, "w+")


def downloadTrack(track: Track, album=None, playlist=None, userProgress=None, partSize=1048576):
    try:
        stream = TIDAL_API.getStreamUrl(track.id, SETTINGS.audioQuality)
        path = getTrackPath(track, stream, album, playlist)

        if SETTINGS.showTrackInfo and not SETTINGS.multiThread:
            Printf.track(track, stream)

        if userProgress is not None:
            userProgress.updateStream(stream)

        # check exist
        if __isSkip__(path, stream.url):
            Printf.success(aigpy.path.getFileName(path) + " already exists")
            return True, ''

        # download
        logging.info("[DL Track] name=" + aigpy.path.getFileName(path) + "\nurl=" + stream.url)

        tool = aigpy.download.DownloadTool(path + '.part', stream.urls)
        tool.setUserProgress(userProgress)
        tool.setPartSize(partSize)
        check, err = tool.start(SETTINGS.showProgress and not SETTINGS.multiThread)
        if not check:
            Printf.err(f"DL Track[{track.title}] failed.{str(err)}")
            return False, str(err)

        # encrypted -> decrypt and remove encrypted file
        __encrypted__(stream, path + '.part', path)

        # contributors
        try:
            contributors = TIDAL_API.getTrackContributors(track.id)
        except:
            contributors = None

        # lyrics
        try:
            lyrics = TIDAL_API.getLyrics(track.id).subtitles
            if SETTINGS.lyricFile:
                lrcPath = path.rsplit(".", 1)[0] + '.lrc'
                aigpy.file.write(lrcPath, lyrics, 'w')
        except:
            lyrics = ''

        __setMetaData__(track, album, path, contributors, lyrics)
        
        # This prints the track title it finished downloading it
        Printf.success(track.title)
        
        return True, ''
    except Exception as e:
        Printf.err(f"DL Track[{track.title}] failed.{str(e)}")
        return False, str(e)


def downloadTracks(tracks, album: Album = None, playlist : Playlist=None):
    def __getAlbum__(item: Track):
        album = TIDAL_API.getAlbum(item.album.id)
        if SETTINGS.saveCovers and not SETTINGS.usePlaylistFolder:
            downloadCover(album)
        return album
    
    if not SETTINGS.multiThread:
        for index, item in enumerate(tracks):
            itemAlbum = album
            if itemAlbum is None:
                itemAlbum = __getAlbum__(item)
                item.trackNumberOnPlaylist = index + 1
            downloadTrack(item, itemAlbum, playlist)
    else:
        thread_pool = ThreadPoolExecutor(max_workers=5)
        for index, item in enumerate(tracks):
            itemAlbum = album
            if itemAlbum is None:
                itemAlbum = __getAlbum__(item)
                item.trackNumberOnPlaylist = index + 1
            thread_pool.submit(downloadTrack, item, itemAlbum, playlist)
        thread_pool.shutdown(wait=True)
