# encoding=utf-8
"""
test file
"""

# print crontab.is_catch_time()


# import nonebot
# from os import path
# import bot.config as config


# if __name__ == '__main__':
#     nonebot.init(config)
#     nonebot.load_plugins(
#         path.join(
#             path.dirname(__file__), 'bot', 'plugins',
#         ),
#         'bot.plugins'
#     )
#     nonebot.run(host='127.0.0.1', port=8080)
from bot.plugins.tawawa.catach_tawawa import pattern
from bot.plugins.tawawa.catach_tawawa.store import judge_should_save

s = '月曜日のたわわ　その２５５ 『チューチューしたい？'

if pattern.is_manga(s) is not None:
    no = pattern.get_no(s)
    res = judge_should_save(no, '578213059')
else:
    pass