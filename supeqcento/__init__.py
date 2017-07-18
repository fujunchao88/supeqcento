# -*- coding: utf-8 -*-
from environs import Env
import platform
import sys
import syslog

from sanic.config import Config, LOGGING
from sanic.defaultFilter import DefaultFilter

_address_dict = {
    'Windows': ('localhost', 514),
    'Darwin': '/var/run/syslog',
    'Linux': '/dev/log',
    'FreeBSD': '/dev/log'
}

CUSTOM_LOGGING = {
    'version': 1,
    'filters': {
        'accessFilter': {
            '()': DefaultFilter,
            'param': [0, 10, 20]
        },
        'errorFilter': {
            '()': DefaultFilter,
            'param': [30, 40, 50]
        }
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]'
                      ' %(message)s]',
            'datefmt': '%y%m%d %H:%M:%S'
        },
        'access': {
            'format': '[%(levelname)1.1s %(asctime)s %(module)s]: %(status)d'
                      ' %(request)s %(message)s %(byte)d',
            'datefmt': '%y%m%d %H:%M:%S'
        }
    },
    'handlers': {
        'internal': {
            'class': 'logging.StreamHandler',
            'filters': ['accessFilter'],
            'formatter': 'simple',
            'stream': sys.stderr
        },
        'accessStream': {
            'class': 'logging.StreamHandler',
            'filters': ['accessFilter'],
            'formatter': 'access',
            'stream': sys.stderr
        },
        'errorStream': {
            'class': 'logging.StreamHandler',
            'filters': ['errorFilter'],
            'formatter': 'simple',
            'stream': sys.stderr
        },
        # before you use accessSysLog, be sure that log levels
        # 0, 10, 20 have been enabled in you syslog configuration
        # otherwise you won't be able to see the output in syslog
        # logging file.
        'accessSysLog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': _address_dict.get(platform.system(),
                                         ('localhost', 514)),
            'facility': syslog.LOG_DAEMON,
            'filters': ['accessFilter'],
            'formatter': 'access'
        },
        'errorSysLog': {
            'class': 'logging.handlers.SysLogHandler',
            'address': _address_dict.get(platform.system(),
                                         ('localhost', 514)),
            'facility': syslog.LOG_DAEMON,
            'filters': ['errorFilter'],
            'formatter': 'simple'
        }
    },
    'loggers': {
        'sanic': {
            'level': 'INFO',
            'handlers': ['internal', 'errorStream']
        },
        'network': {
            'level': 'INFO',
            'handlers': ['accessStream', 'errorStream']
        }
    }
}

LOGGING.update(CUSTOM_LOGGING)

Config.LOGO = "SUPEQCENTO GO FAST!"


def load_env(self):
    env = Env()
    env.read_env()
    self['DB_PARAMS'] = env.dict('DB_PARAMS')

Config.load_environment_vars = load_env
