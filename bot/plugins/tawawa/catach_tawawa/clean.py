from lxml import etree
from bot.plugins.tawawa.catach_tawawa import pattern


# find target picture link and file name from html
def find_twitter(o_html):
    # init html with etree lib
    html = etree.HTML(o_html)
    result = html.xpath('//div[@class="content"]')

    for i in result:
        t_html = etree.tostring(i)
        t_html = etree.HTML(t_html)

        s_html = t_html

        # get the twitter body text with xpath
        x = t_html.xpath('//div[@class="js-tweet-text-container"]/p/text()')

        # remove \s \t etc char
        s = x[0].encode('utf-8')
        s = s.decode('utf-8')
        s = "".join(s.split())

        # only find the first result, if find it, return link and picture number
        if pattern.is_manga(s) is not None:
            link = catch_image(s_html)
            if link is not False:
                no = pattern.get_no(s)
                return [link, no]
        else:
            continue

    # if doesn't find, return None
    return [None, None]


# find image link from twitter
def catch_image(target_html):
    link = target_html.xpath('//div[@class="AdaptiveMedia-container"]//img/@src')
    if len(link) > 0:
        return link[0]
    else:
        return False
