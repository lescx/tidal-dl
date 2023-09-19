#!/usr/bin/env python

class LangEnglish(object):
    SETTING = "SETTINGS"
    VALUE = "VALUE"

    CHOICE = "CHOICE"
    FUNCTION = "FUNCTION"
    CHOICE_ENTER = "Enter"
    CHOICE_LOGIN = "Check AccessToken"
    CHOICE_SETTINGS = "Settings"
    CHOICE_SET_ACCESS_TOKEN = "Set AccessToken"
    CHOICE_LOGOUT = "Logout"
    CHOICE_APIKEY = "Select APIKey"

    PRINT_ERR = "Error:"
    PRINT_INFO = "Info:"
    PRINT_SUCCESS = "Success:"

    PRINT_ENTER_CHOICE = "Enter Choice:"
    PRINT_LATEST_VERSION = "Latest version:"

    # {} are required in these strings
    AUTH_START_LOGIN = "Starting login process..."
    AUTH_LOGIN_CODE = "Your login code is {}"
    AUTH_NEXT_STEP = "Go to {} within the next {} to complete setup."
    AUTH_WAITING = "Waiting for authorization..."
    AUTH_TIMEOUT = "Operation timed out."

    MSG_VALID_ACCESSTOKEN = "AccessToken good for {}."
    MSG_INVALID_ACCESSTOKEN = "Expired AccessToken. Attempting to refresh it."
    MSG_PATH_ERR = "File path error!"
    MSG_INPUT_ERR = "Input error!"

    MODEL_ALBUM_PROPERTY = "ALBUM-PROPERTY"
    MODEL_TRACK_PROPERTY = "TRACK-PROPERTY"
    MODEL_VIDEO_PROPERTY = "VIDEO-PROPERTY"
    MODEL_ARTIST_PROPERTY = "ARTIST-PROPERTY"
    MODEL_PLAYLIST_PROPERTY = "PLAYLIST-PROPERTY"

    MODEL_TITLE = 'Title'
    MODEL_TRACK_NUMBER = 'Track Number'
    MODEL_VIDEO_NUMBER = 'Video Number'
    MODEL_RELEASE_DATE = 'Release Date'
    MODEL_VERSION = 'Version'
    MODEL_EXPLICIT = 'Explicit'
    MODEL_ALBUM = 'Album'
    MODEL_ID = 'ID'
    MODEL_NAME = 'Name'
    MODEL_TYPE = 'Type'
