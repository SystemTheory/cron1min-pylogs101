import os

# Name of log files
LOGFILE_NAME = 'cron1min.log'
DEBUGFILE_NAME = 'cron1min.dbg'

# Logging handler level
CONSOLE_LEVEL = 'INFO'
FILE_LEVEL = 'INFO'
DEBUG_LEVEL = 'DEBUG'

# Do not make changes in this section
THIS_PATH = os.path.abspath(__file__)
THIS_DIR = os.path.split(THIS_PATH)[0]
LOGFILE_PATH = THIS_DIR + '/' + LOGFILE_NAME
DEBUGFILE_PATH = THIS_DIR + '/' + DEBUGFILE_NAME

# logging configuration dictionary
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'NOTSET',
        'handlers': [
            'console',
            'file',
#            'debug'
        ]
    },
    'loggers': {

    },
    'formatters': {
        'datetimeday': {
            'format': '%(asctime)-15s %(levelname)-7s %(dayofweek)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': CONSOLE_LEVEL,
            'formatter': 'datetimeday',
            'stream': 'ext://sys.stdout',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': FILE_LEVEL,
            'formatter': 'datetimeday',
            'mode': 'a', # append mode
            'filename': LOGFILE_PATH,
            'class': 'logging.FileHandler', # file does not rotate
        },
        'debug': {
            'level': DEBUG_LEVEL,
            'formatter': 'datetimeday',
            'mode': 'a', # append mode
            'filename': DEBUGFILE_PATH,
            'class': 'logging.FileHandler', # file does not rotate
        },
    },
}
