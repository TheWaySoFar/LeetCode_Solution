#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#抓取https://www.python.org/events/python-events/会议的时间地点
from html.parser import HTMLParser
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.flag, self.time, self.location, self.title = False, False, False, False

    def get_attrs(self, attrs, name):
        for attr in attrs:
            if attr[0] == name:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and self.get_attrs(attrs, "class") == "list-recent-events menu":
            self.flag = True
        elif tag == 'h3' and self.flag == True and self.get_attrs(attrs, "class") == "event-title":
            self.title = True

        elif tag == 'time' and self.flag == True:
            self.time = True

        elif tag == 'span' and self.flag == True and self.get_attrs(attrs, "class") == "event-location":
            self.location = True


    def handle_endtag(self, tag):
        if tag == 'h3' and self.flag == True and self.title == True:
            self.title = False
        elif tag == 'time' and self.flag and self.time:
            self.time = False
        elif tag == 'span' and self.flag and self.location:
            self.location = False
        if tag == 'ul' and self.flag:
            self.flag = True

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.flag and self.title:
            print("Title : ", data)
            self.title = False
        if self.flag and self.time:
            print("Time : ", data)
            self.time = False
        if self.flag and self.location:
            print("Location : ", data)
            self.location = False

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

if __name__ == '__main__':
    parser = MyHTMLParser()
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    #print(data)
    parser.feed(data)