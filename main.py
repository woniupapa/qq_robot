# encoding=utf-8
"""
test file
"""

# print crontab.is_catch_time()


import nonebot
from os import path
import bot.config as config


if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(
            path.dirname(__file__), 'bot', 'plugins',
        ),
        'bot.plugins'
    )
    nonebot.run(host='0.0.0.0', port=8080)
