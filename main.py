"""
main file
"""

import nonebot
from os import path
import bot.config.bot_config as config


if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(
            path.dirname(__file__), 'bot', 'plugins',
        ),
        'bot.plugins'
    )
    nonebot.run(host=config.HOST, port=config.PORT)
