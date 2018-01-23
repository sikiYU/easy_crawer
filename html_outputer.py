# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    """docstring for HtmlOutputer"""

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<div>")
        for data in self.datas:
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])
        fout.write("</div>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
