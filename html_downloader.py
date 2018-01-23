# -*- coding: utf-8 -*-

import urllib
from urllib import request
from urllib.parse import quote
import string


class HtmlDownloader(object):
    """docstring for HtmlDownloader"""

    def download(self, url):
        if url is None:
            return None
        url = quote(url, safe=string.printable)
        res = urllib.request.urlopen(url)
        if res.getcode() != 200:
            return None
        return res.read()
