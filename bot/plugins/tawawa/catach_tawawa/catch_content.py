import requests
from bot.plugins.tawawa import config


# get html content from twitter
def get_twitter():
    url = config.target_url
    handle = requests.session()
    response = handle.get(url, timeout=20)
    if response.status_code != 200:
        return ['获取Twitter内容失败', False]
    html = response.text
    return [html, True]


# get watata picture from link
def get_png(link):
    png = requests.get(link)
    return png.content
