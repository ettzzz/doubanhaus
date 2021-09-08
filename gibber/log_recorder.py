#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:39:54 2021

@author: eee
"""

import os
import logging
import logging.config

from config.static_vars import ROOT, DEBUG, LOGGING_FMT, LOGGING_DATE_FMT


def get_logger(debug=DEBUG):
    '''
    # # print log info
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    '''
    # create logger
    logger_name = "doubanhaus_logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if not debug:
        # create formatter
        formatter = logging.Formatter(LOGGING_FMT, LOGGING_DATE_FMT)

        # create file handler
        log_path = os.path.join(ROOT, 'haus.log')
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.INFO)

        # add handler and formatter to logger
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger


