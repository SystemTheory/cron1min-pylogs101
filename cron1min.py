#!/usr/bin/env python3

import appconf
import logging
import datetime
import calendar
import logging.config

CONFIG_LOG = appconf.LOG_CONFIG

class LogFilter(logging.Filter):
    """ This is a filter which injects contextual info into the log. """
    def filter(self, record):
        now = datetime.datetime.today()
        day_int = now.weekday()
        dayofweek = calendar.day_abbr[day_int]
        record.dayofweek = dayofweek
        return True

logging.config.dictConfig(CONFIG_LOG)
logger = logging.getLogger(__name__)
filt = LogFilter()
logger.addFilter(filt)

now = datetime.datetime.today()
day_int = now.weekday()
if 0 <= day_int <= 4: # Mon[0], Tue[1], Wed[2], Thu[3], Fri[4]
    logger.info('Cron fired!')
    logger.debug(str(day_int) + ' = day_int')
if 5 <= day_int <= 6: # Sat[5], Sun[6]
    logger.info('Cron fired')
    logger.debug(str(day_int) + ' = day_int')
