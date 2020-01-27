import os

pic_search_link = 'https://www.pixiv.net/artworks/'

plugin_path = os.path.dirname(__file__)

src_path = plugin_path + '/src'

db_path = src_path + '/db'

bd_file = db_path + '/pixiv.db'
ddl_file = db_path + '/ddl.py'
