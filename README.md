# `tidal-dl` – "Tidal Media Downloader" fork

`tidal-dl` is a fork of [Tidal-Media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader). It lets you download videos and tracks from Tidal.

## Disclaimer

- Private use only.
- You need a paid Tidal-HIFI subscription.
- You must not use this method for music distribution or piracy.
- It may be illegal to use `tidal-dl` in your country.

## Installation / Developing 

<!-- ```shell
pip3 install tidal-dl --upgrade
``` -->

```shell
python3 -m venv tidal-dl
source venv/bin/activate
pip3 uninstall tidal-dl
pip3 install -r requirements.txt --user
python3 setup.py install
```

And when you are done developing:

```shell
deactivate
```

## Usage

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

If you really like my projects and want to support me, you can [buy Yaronzz a coffee](https://www.buymeacoffee.com/yaronzz).

Please consider leaving a star on the original project or my fork.

## Contributors

I thank [yaronzz](https://github.com/yaronzz) for creating this tool initially!

This project exists thanks [to all the people who contribute](https://github.com/yaronzz/Tidal-Media-Downloader/graphs/contributors). 

## Libraries and reference

- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)

## License

This project is licensed under The Apache Version 2.0 License. More information can be found [here](https://github.com/yaronzz/Tidal-Media-Downloader/blob/master/LICENSE)
