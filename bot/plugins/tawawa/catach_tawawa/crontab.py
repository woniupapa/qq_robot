import os
import time
from bot.plugins.tawawa.catach_tawawa import config

# set default timezone
os.environ['TZ'] = config.TZ

def is_catch_time():
    week = time.strftime("%w", time.localtime())

    if week == 1 or week == 0:
        return True

    return False


def sleep(min):
    time.sleep(min)
