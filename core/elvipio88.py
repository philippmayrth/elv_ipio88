#! /usr/bin/env python
#
# Created by Philipp Mayr on 27. June, 2013 (Germany)
#
# Name: elvipio88.py
#
# License: CC NY-NC
#

"""
# Usage:
    
from core.elvipio88 import elvipio88 as iodevice

io = iodevice("192.168.1.100")
print io.getport()
"""

import urllib
from core.BeautifulSoup import BeautifulSoup


class elvipio88:
    soup = None
    
    def __init__(self, address="192.168.1.100"):
        self.address = address
    
    def getsoup(self):
        htmlsoup = urllib.urlopen("http://"+self.address+"/ipio.cgi").read()
        soup = BeautifulSoup(htmlsoup)
        self.soup = soup
        return False
    
    def getport(self):
        if self.soup == None:
            self.getsoup()
        if self.soup == False:
            return True
        
        # isolate lines containing port state
        pfiltered = self.soup.findAll("input", type="checkbox")
        rlist = []
        for pnr in range(16):
            pstate = "checked" in str(pfiltered[pnr]) # returns True or False
            rlist.append(pstate)
        return rlist

    def setport(self, newpstate):
        pass

    
