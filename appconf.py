import os
import logging
import datetime
import calendar

# Name of log files
LOGFILE_NAME = 'cron1min.info'
DEBUGFILE_NAME = 'cron1min.dbug'

# Logging handler level
CONSOLE_LEVEL = 'INFO'
FILE_LEVEL = 'INFO'
DEBUG_LEVEL = 'DEBUG'

# Do not make changes in this section
THIS_PATH = os.path.abspath(__file__)
THIS_DIR = os.path.split(THIS_PATH)[0]
LOGFILE_PATH = THIS_DIR + '/' + LOGFILE_NAME
DEBUGFILE_PATH = THIS_DIR + '/' + DEBUGFILE_NAME

# Specify logging filter
class DayFilter(logging.Filter):
    """ Inserts day of week into log entries. """
    def filter(self, record):
        day_int = datetime.datetime.today().weekday()
        dayofweek = calendar.day_abbr[day_int]
        record.dayofweek = dayofweek
        return True

# logging configuration dictionary
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'dayfilter': {
            '()': DayFilter,
        },
    },
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
            'filters': ['dayfilter'],
            'formatter': 'datetimeday',
            'stream': 'ext://sys.stdout',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': FILE_LEVEL,
            'filters': ['dayfilter'],
            'formatter': 'datetimeday',
            'mode': 'a', # append mode
            'filename': LOGFILE_PATH,
            'class': 'logging.FileHandler', # file does not rotate
        },
        'debug': {
            'level': DEBUG_LEVEL,
            'filters': ['dayfilter'],
            'formatter': 'datetimeday',
            'mode': 'a', # append mode
            'filename': DEBUGFILE_PATH,
            'class': 'logging.FileHandler', # file does not rotate
        },
    },
}
