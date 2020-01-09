import re
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand, permission

from bot.plugins.repeat.repeat import Repeat


@on_command('repeat', only_to_me=False, permission=permission.GROUP)
async def repeat(session: CommandSession):
    msg_type = session.ctx['message_type']
    at_me = session.ctx['to_me']
    user_no = session.ctx['user_id']
    group_id = session.ctx['group_id']
    msg_obj = session.ctx['message']

    if msg_type != 'group' or at_me:
        return

    if user_no == 1000000:
        return

    for seg in msg_obj:
        m_type = seg['type']
        if m_type not in ['text', 'image']:
            return

        if m_type == 'text':
            msg_str = seg['data']['text']
            if re.match("^[.*?]你的QQ暂不支持", msg_str) is not None:
                return

    repeater = Repeat()

    is_repeat = repeater.push_group_msg(group_id, msg_obj)
    if is_repeat:
        await session.send(msg_obj)
    else:
        return

@repeat.args_parser
async def _(session: CommandSession):
    pass


@on_natural_language(only_to_me=False, permission=permission.GROUP)
async def _(session: NLPSession):
    if session.ctx['to_me']:
        return

    return IntentCommand(60.0, 'repeat')
