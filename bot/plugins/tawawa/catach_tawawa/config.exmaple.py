# encoding=utf-8

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


# get witch watata number should be catch now
def should_catch_no(qq_number):
    import os
    if not os.path.exists('lock/lock_no_' + qq_number):
        return 0

    with open('lock/lock_no_' + qq_number, 'r+') as f:
        no = f.read()

    return no


# email info
sender_name = 'example_sender@sender.com'  # sender's email address
sender_pass = 'sender_pass'  # sender's email password

receiver = 'example_receiver@receive.com'  # receiver's email address

# SMTP config
smtp_server = 'smtp.example.com'  # smtp server address
smtp_port = 999  # smtp server port

TZ = 'Asia/Tokyo'  # default timezone setting

log_path = 'log/logging.log'  # default logging path
