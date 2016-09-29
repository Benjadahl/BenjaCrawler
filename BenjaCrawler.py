#!/usr/bin/env python3

import time
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

sourceSite = sys.argv[1]
maxSite = sys.argv[2]

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
                #Checks for relative domains
                href = element["href"]
                if (href[0] == "/"):
                    href = self.url + href
                self.links.append(href)
        except Exception:
            print("Error while gettings links for: " + self.url)

queue = [site("http://dr.dk")]
crawledLinks = {}
text = ""

"""STARTUP CODE"""
print("Starting benjaCrawler for site: " + sourceSite)
startTime = time.time()

for i in range(0, int(maxSite)):
    queue[i].dlSite()
    queue[i].makeSoup()
    queue[i].getHref()
    text += queue[i].url + "\n"
    for link in queue[i].links:
        if(not hasattr(crawledLinks, link)):
            text += "    " + link + "\n"
            queue.append(site(link))
            crawledLinks[link] = True
            #print(link)
    print("Crawled " + str(i + 1) + " links")
print("Done crawling saving result to crawl.txt \n    Thank you for crawling with BenjaCrawler \n   "  + str(time.time() - startTime) + " seconds")
f = open("crawl.txt","w")
f.write(text)
f.close()
