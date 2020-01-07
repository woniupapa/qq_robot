# encoding=utf-8

import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

from bot.plugins.tawawa.catach_tawawa import config


def send_email(no, att_path, file_name):
    my_sender = config.sender_name
    my_pass = config.sender_pass
    my_user = config.receiver

    smtp_server = config.smtp_server
    smtp_port = config.smtp_port

    def mail():
        ret = True
        try:
            msg = MIMEMultipart()
            msg['From'] = formataddr(["月曜日のたわわ", my_sender])
            msg['To'] = formataddr(["receiver", my_user])
            msg['Subject'] = "月曜日のたわわ その%s" % no

            msg.attach(MIMEText("月曜日のたわわ その%s" % no))

            att1 = MIMEApplication(open(att_path, 'rb').read(), name=file_name)
            att1["Content-Disposition"] = 'attachment; filename="%s"' % file_name
            msg.attach(att1)

            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            server.login(my_sender, my_pass)
            server.sendmail(my_sender, [my_user, ], msg.as_string())
            server.quit()
        except Exception as e:
            ret = False
        return ret

    ret = mail()
    if ret:
        return False
    else:
        return True
