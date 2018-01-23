# -*- coding: utf-8 -*-
import url_manager, html_downloader, html_paser, html_outputer


class Spider(object):
    """docstring for Spider"""

    def __init__(self):
        self.urls = url_manager.UrlManager()  # url list
        self.downloader = html_downloader.HtmlDownloader()  # 根据提供的url下载相应html
        self.paser = html_paser.HtmlPaser()  # 解析html页面
        self.outputer = html_outputer.HtmlOutputer()  # 数据

    def craw(self, base_url):
        self.urls.add_new_url(base_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.paser.parse(new_url, html_content)  # 获取页面urls，添加到url list中
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == "__main__":
    base_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    spider = Spider()
    spider.craw(base_url)
