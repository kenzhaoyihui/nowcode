#!/usr/bin/env python2.7
import re
from HTMLParser import HTMLParser
import urllib2

# class MyHTMLParse(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         """
#         recognize start tag, like <div>
#         : param tag:
#         : param attrs:
#         : return:
#         """

#         print ("Encountered a start tag: ", tag)

#     def handle_endtag(self, tag):
#         """
#         recognize end tag, like </div>
#         : param tag:
#         : return:
#         """

#         print ("Encountered an end tag: ", tag)

#     def handle_data(self, data):
#         """
#         recognize data, html content string
#         : param data:
#         : return:
#         """
#         #if self.lasttag == "title":
#         print ("Encountered some data: ", data)

#     def handle_startendtag(self, tag, attrs):
#         """
#         recognize tag that without endtag, like <img />
#         : param tag:
#         : param attrs:
#         : return:
#         """

#         print ("Encountered startendtag: ", tag)

#     def handle_comment(self, data):
#         """
#         : param data:
#         : return:
#         """

#         print ("Encountered comment: ", data)

# parser = MyHTMLParse()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1><img src= "" />'
#             '<!-- comment --></body></html>')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.a_texts = []
        self.a_text_flag = False

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            self.a_text_flag = True
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)
                        
    def handle_endtag(self, tag):
        if tag == "a":
            self.a_text_flag = False

    def handle_data(self, data):
        if self.a_text_flag:
            if data.startswith("rhvm-appliance"):
                self.a_texts.append(data)


def get_url_html(rhvm_appliance_path):
    req = urllib2.Request(rhvm_appliance_path)
    response = urllib2.urlopen(req)
    html = response.read()

    mp = MyHTMLParser()
    mp.feed(html)
    mp.close()

    mp.a_texts.sort()

    link_42 = []

    for link in mp.a_texts:
        if "4.2" in link:
            link_42.append(link)

    latest_rhvm_appliance_name = link_42[-1]
    """
    latest_rhvm_appliance_link = None
    for link in mp.links:
        if re.search(latest_rhvm_appliance_name, link):
            latest_rhvm_appliance_link = link
    """
    latest_rhvm_appliance = rhvm_appliance_path + latest_rhvm_appliance_name

    return latest_rhvm_appliance


if __name__ == '__main__':
    print get_url_html("http://10.66.10.22:8090/rhevm-appliance/")