from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from bot.plugins.tawawa.catach_tawawa import log
from .config import *
import bot.plugins.tawawa.catach_tawawa.action as action
from .helper import *


@on_command('tawawa')
async def tawawa(session: CommandSession):
    await session.send('123')
    # qq_number = '10000'  # todo it should be catch from session
    # try:
    #     msg, ok, no = action.start(qq_number)
    #     print([msg, ok, no])
    #     log.write([msg, ok, no])
    #     if ok is False:
    #         await session.send(msg)
    #     else:
    #         prev_msg = '现在发送第' + str(no) + '话'
    #         await session.send(prev_msg)
    #
    #         b64_str = get_b64_content(msg)
    #         seg = MessageSegment.image(b64_str)
    #         await session.send(seg)
    # except Exception as e:
    #     log.write(e)
    #     await session.send('发生了些小小的错误呢')


@tawawa.args_parser
async def _(session: CommandSession):
    pass


@on_natural_language(keywords=nlp_keywords)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'tawawa')