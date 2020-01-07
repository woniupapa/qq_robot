import logging
from bot.plugins.tawawa.catach_tawawa import config
import os

log_path = config.log_path

if not os.path.exists(os.path.dirname(log_path)):
    os.mkdir(os.path.dirname(log_path))

logging.basicConfig(filename='log/logger.log')


def write(msg):
    logging.log(logging.ERROR, msg)
