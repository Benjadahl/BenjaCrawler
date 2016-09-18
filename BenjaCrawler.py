#!/usr/bin/env python3

import wget
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

class site(object):
    def __init__(self, url):
        self.url = url
        self.time = time.time()
        self.links = []

    def dlSite(self):
        try:
            self.html = urlopen(self.url).read()
        except Exception:
            print("Error while downloading site: " + self.url)

    def makeSoup(self):
        try:
            self.soup = BeautifulSoup(self.html, "lxml")
        except Exception:
            print("Error while making soup for: " + self.url)

    def getHref(self):
        try:
            self.aTags = self.soup.findAll("a")
            for element in self.aTags:
                #Should add check for relative domains
                self.links.append(element["href"])
        except Exception:
            print("Error while gettings links for: " + self.url)

queue = [site("http://rend.al")]

for i in range(0, 150):
    queue[i].dlSite()
    queue[i].makeSoup()
    queue[i].getHref()
    for link in queue[i].links:
        queue.append(site(link))
    print(queue[i].links)
    print("Crawled " + str(i) + " links")
