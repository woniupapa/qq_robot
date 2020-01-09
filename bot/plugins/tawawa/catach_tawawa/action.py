from bot.plugins.tawawa.catach_tawawa import catch_content, clean, log, store


def action(qq_number):
    html, ok = catch_content.get_twitter()

    if ok is not True:
        return [html, ok, None]

    link, no = clean.find_twitter(html)

    if link is None or no is None:
        return ["啥都没有呢", False, no]  # response message 'nothing catch'

    if store.judge_should_save(no, qq_number) is False:
        # return ['最新的漫画还没有发布~', False, store.get_full_path(no)]  # response message 'still don't have newest comic'
        return [store.get_full_path(no), True, no]  # todo now return full path without any tips

    watata_picture = catch_content.get_png(link)
    full_path, ok = store.save_png(watata_picture, no, qq_number)

    return [full_path, ok, no]


# main execute function
def start(qq_number):
    qq_number = str(qq_number)
    res = action(qq_number)  # it will start catch immediately after start script
    return res
    # try:
    #     res = action(qq_number)  # it will start catch immediately after start script
    #     return res
    # except Exception as e:
    #     log.write(e)
    #     return ['获取漫画的时候发生了一些错误~', False, None]
