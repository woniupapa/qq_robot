# strange stone's twitter home page
target_url = 'https://twitter.com/Strangestone?lang=ja'

# the comparison table of en number and jp number
number_translation_table = {
    '1': '１',
    '2': '２',
    '3': '３',
    '4': '４',
    '5': '５',
    '6': '６',
    '7': '７',
    '8': '８',
    '9': '９',
    '0': '０',
}

tawawa_nlp_keywords = {
    '真正的周一',
    '周一还没开始',
    '星期一还没开始',
    '周一的丰满',
    '星期一的丰满',
    '真正的星期一',
    '开启真正的周一'
    '周一启动',
}


# get witch watata number should be catch now
def should_catch_no(qq_number):
    import os
    if not os.path.exists('lock/lock_no_' + qq_number):
        return 0

    with open('lock/lock_no_' + qq_number, 'r+') as f:
        no = f.read()

    return no

TZ = 'Asia/Tokyo'

log_path = 'log/logging.log'
