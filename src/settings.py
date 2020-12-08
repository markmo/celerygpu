import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

APPNAME = os.environ['APPNAME']

CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']

CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']

ONCE = {
  'backend': 'celery_once.backends.Redis',
  'settings': {
    'url': CELERY_BROKER_URL,
    'default_timeout': 60
  }
}