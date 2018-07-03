#!usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")



from logging.handlers import RotatingFileHandler
"""
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp1.log',
                    filemode='w')

# define a StreamHandler()
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# define a RotatingFileHandler
Rthandler = RotatingFileHandler('myapp2.log', maxBytes=10*1024*1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)

"""
logger.debug('This is debug message!')
logger.info('This is info message!')
logger.warning('This is warning message!')

