import nonebot
from nonebot import CommandSession


@nonebot.scheduler.scheduled_job('cron', hour='*', minute='*', second='*')
async def x(session: CommandSession):
    bot = nonebot.get_bot()