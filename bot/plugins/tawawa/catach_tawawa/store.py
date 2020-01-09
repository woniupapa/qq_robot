from bot.plugins.tawawa import config
import os


# check if the manga should be store and send email
def judge_should_save(no, qq_number):
    should_no = int(config.should_catch_no(qq_number))
    no = int(no)

    if no <= should_no:
        return False

    return True


# save png to local and send email
def save_png(source, no, qq_number):
    full_path = get_full_path(no)

    # write picture source into file
    with open(full_path, 'wb+') as f:
        f.write(source)

    # update lock number
    with open('lock/lock_no_' + qq_number, 'w+') as f:
        f.write(no)

    return [full_path, True]


def get_full_path(no):
    file_name = 'tawawa_' + no + '.png'

    current_path = os.path.dirname(__file__)

    # the path without filename
    path = os.path.join(current_path, 'tawawa_picture')

    # create directory if it isn't exist
    if not os.path.exists(path):
        os.mkdir(path)

    # the path contain filename
    full_path = os.path.join(path, file_name)

    return full_path
