# `tidal-dl` – "Tidal Media Downloader"

`tidal-dl` lets you archive music from Tidal.

I forked [Yaronzz](https://github.com/yaronzz/Tidal-Media-Downloader) project after it developed in the wrong direction and in a slow pace in my opinion. Still, this project uses many lines of the original code under the hood.

## Disclaimer

* Private use only.
* You need a paid Tidal-HIFI subscription.
* You are not allowed to use this to share or pirate music.
* It may be illegal to use `tidal-dl` in your country.

## Installation / Developing 

### 0. Prerequisites

* Make sure you have Python 3.11 or higher installed on your system.
* Install [Poetry](https://python-poetry.org) if you haven't already (it's great!). You can install it using pipx:

```shell
pipx install poetry
```

For other installation methods, see Poetry's [official docs](https://python-poetry.org/docs/).

### 1. Install Dependencies with Poetry

Use Poetry to install the project's dependencies and set up a python `venv` virtual environment:

```shell
poetry install
```

This command will create a virtual environment for your project and install all required dependencies listed in `pyproject.toml`.

### 2. Activate the Virtual Environment

If you want to activate the virtual environment to work within it, you can use:

```shell
poetry shell
```

Activating the virtual environment is optional but highly recommended.

### (Do Your Development and) Run Your Program

```shell
poetry run python tidal_dl/__init__.py
```

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


## Support

If you really like this project and want to say thank you, you can [buy Yaronzz a coffee](https://www.buymeacoffee.com/yaronzz). He will thank you personally every morning!

Please consider leaving a star if you use this script.

## Contributors

I thank [Yaronzz](https://github.com/yaronzz) for creating this tool initially.

## Libraries and reference

- [Tidal-media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader)
- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)

## License

This project is licensed under The Apache Version 2.0 License. More information can be found [here](https://github.com/lescx/tidal-dl/blob/main/LICENSE)
