# encoding=utf-8

import re
from bot.plugins.tawawa import config


# get watata number
def get_no(string):
    string = delete_blank(string)
    no = re.findall('その(.+?)『', string)

    if len(no) > 0:
        return translate_no(no[0])
    else:
        return 'unknown'


# check if the twitter is tawawa manga
def is_manga(string):
    # delete blank inside string
    string = delete_blank(string)

    pattern = '月曜日のたわわその(１|２|３|４|５|６|７|８|９|０){3}『'
    res = re.match(pattern, string, flags=0)

    return res


# translate jp numbers to the en numbers
def translate_no(no):
    re_list = config.number_translation_table
    for num, jp_num in re_list.items():
        no = re.sub(jp_num, num, no)

    return no


def delete_blank(string):
    # delete blank inside string
    string = ''.join(string.split('　'))
    string = ''.join(string.split(' '))
    return string
