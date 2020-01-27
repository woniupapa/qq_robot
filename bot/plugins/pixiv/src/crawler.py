import requests

from bot.plugins.pixiv import config


class PixiviCrawler:
    req = None
    p_search_link = ''
    search_key = ''

    def __init__(self):
        self.req = requests.session()
        self.p_search_link = config.pic_search_link

    def search(self, key=''):
        target_link = self.p_search_link

    def download_html(self):
        pass
