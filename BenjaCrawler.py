#!/usr/bin/env python3

import wget
import time

class site(object):
    def __init__(self, url):
        self.url = url
        self.time = time.time()

    def dlSite(self):
        try:
            filename = wget.download(self.url)
        except Exception:
            print("Error while downloading site: " + self.url)
        #return filename

site1 = site("http://www.google.com")

print(site1.dlSite())
