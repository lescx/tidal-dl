# `tidal-dl` – Tidal Media Downloader

`tidal-dl` is a fork of [Tidal-Media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader). It lets you download videos and tracks from Tidal.

## Disclaimer

- Private use only.
- Need a paid Tidal-HIFI subscription. 
- You should not use this method to distribute or pirate music.
- It may be illegal to use this in your country, so be informed.

## Installation 

```shell
pip3 install tidal-dl --upgrade
```

| USE                                                   | FUNCTION                   |
| ----------------------------------------------------- | -------------------------- |
| tidal-dl                                              | Show interactive interface |
| tidal-dl -h                                           | Show help-message          |
| tidal-dl -l "https://tidal.com/browse/track/70973230" | Download link              |
| tidal-dl -g                                           | Show simple-gui            |

## Settings - Possible Tags

### Album

| Tag               | Example value                         |
| ----------------- | ------------------------------------- |
| {ArtistName}      | The Beatles                           |
| {AlbumArtistName} | The Beatles                           |
| {Flag}            | M/A/E *(Master/Dolby Atmos/Explicit)* |
| {AlbumID}         | 55163243                              |
| {AlbumYear}       | 1963                                  |
| {AlbumTitle}      | Please Please Me (Remastered)         |
| {AudioQuality}    | LOSSLESS                              |
| {DurationSeconds} | 1919                                  |
| {Duration}        | 31:59                                 |
| {NumberOfTracks}  | 14                                    |
| {NumberOfVideos}  | 0                                     |
| {NumberOfVolumes} | 1                                     |
| {ReleaseDate}     | 1963-03-22                            |
| {RecordType}      | ALBUM                                 |
| {None}            |                                       |

### Track

| Tag               | Example Value                              |
| ----------------- | ------------------------------------------ |
| {TrackNumber}     | 01                                         |
| {ArtistName}      | The Beatles                                |
| {ArtistsName}     | The Beatles                                |
| {TrackTitle}      | I Saw Her Standing There (Remastered 2009) |
| {ExplicitFlag}    | (*Explicit*)                               |
| {AlbumYear}       | 1963                                       |
| {AlbumTitle}      | Please Please Me (Remastered)              |
| {AudioQuality}    | LOSSLESS                                   |
| {DurationSeconds} | 173                                        |
| {Duration}        | 02:53                                      |
| {TrackID}         | 55163244                                   |

### Video

| Tag               | Example Value                              |
| ----------------- | ------------------------------------------ |
| {VideoNumber}     | 00                                         |
| {ArtistName}      | DMX                                        |
| {ArtistsName}     | DMX, Westside Gunn                         |
| {VideoTitle}      | Hood Blues                                 |
| {ExplicitFlag}    | (*Explicit*)                               |
| {VideoYear}       | 2021                                       |
| {TrackID}         | 188932980                                  |

## Support

If you really like my projects and want to support me, you can [buy Yaronzz a coffee](https://www.buymeacoffee.com/yaronzz) and star its project or my fork.

## Contributors

I thank [yaronzz](https://github.com/yaronzz) for creating this tool initially!

This project exists thanks [to all the people who contribute](https://github.com/yaronzz/Tidal-Media-Downloader/graphs/contributors). 

## Libraries and reference

- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)

## Developing

```shell
pip3 uninstall tidal-dl
pip3 install -r requirements.txt --user
python3 setup.py install
```

## License

- [License](https://github.com/lescx/tidal-dl/blob/master/LICENSE)
