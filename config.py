import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    CACHE_TYPE = os.environ.get('CACHE_TYPE') or 'NullCache'
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_DEFAULT_TIMEOUT')) or 0
    CACHE_DIR = os.environ.get('CACHE_DIR') or 'cache'
