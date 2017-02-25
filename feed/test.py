#-*- coding: utf-8 -*-

import feedparser
import re
from urllib.request import urlopen


def fetch_feed(url):
    d = feedparser.parse(url)
    if d.entries:
        for post in d.entries:
            print('title: {}\n'.format(post.title.encode('utf8')))
            print('link: {}\n'.format(post.link))
            print('desc: {}\n\n\n'.format(post.description))


fetch_feed("http://daringfireball.net/feeds/main")
