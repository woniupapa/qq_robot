from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand, permission


@on_command('pixiv', permission=permission.GROUP)
async def repeat(session: CommandSession):
    msg_type = session.ctx['message_type']
    at_me = session.ctx['to_me']
    user_no = session.ctx['user_id']
    group_id = session.ctx['group_id']
    msg_obj = session.ctx['message']


@repeat.args_parser
async def _(session: CommandSession):
    pass


@on_natural_language(only_to_me=False, permission=permission.GROUP)
async def _(session: NLPSession):
    return IntentCommand(60.0, 'repeat')
