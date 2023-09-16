# `tidal-dl` – "Tidal Media Downloader"

`tidal-dl` is a fork of [Tidal-Media-Downloader](https://github.com/yaronzz/Tidal-Media-Downloader). It lets you download videos and tracks from Tidal.

You can read about the [reasons for the fork]() below.

## Disclaimer

- Private use only.
- You need a paid Tidal-HIFI subscription.
- You must not use this method for music distribution or piracy.
- It may be illegal to use `tidal-dl` in your country.

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

## Usage

| USE                                                   | FUNCTION                   |
| ----------------------------------------------------- | -------------------------- |
| tidal-dl                                              | Show interactive interface |
| tidal-dl -h                                           | Show help-message          |
| tidal-dl -l "https://tidal.com/browse/track/70973230" | Download link              |

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

If you really like this project and want to say thank you, you can [buy Yaronzz a coffee](https://www.buymeacoffee.com/yaronzz).

Please consider leaving a star on the original project or my fork.

## Contributors

I thank [Yaronzz](https://github.com/yaronzz) for creating this tool initially!

This project exists thanks [to all the people who contribute](https://github.com/yaronzz/Tidal-Media-Downloader/graphs/contributors). 

## Libraries and reference

- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)

## Why a fork?

Der Hauptgrund sind überflüssige Anti-Features und schlechte design-Entscheidungen in der Entwicklung, die mich während der Benutzung geärgert haben.

Bei meinem fork lege ich deshalb besonderen Wert auf:

- Folgen aktueller best practices
- besser keine GUI als eine halbherzig implementierte GUI
- keine unnötigen Abhängigkeiten
- Implementierung der UNIX-Philosophy (insofern das in ein Python-tool möglich ist)

## License

This project is licensed under The Apache Version 2.0 License. More information can be found [here](https://github.com/yaronzz/Tidal-Media-Downloader/blob/master/LICENSE)
