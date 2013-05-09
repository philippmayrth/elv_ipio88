"""
Autor: https://www.facebook.com/philipp.mayr.th
Date: 28. May, 2012 (germany)

this is an API for the 'ELV IPIO 88'
Read 'in' ports and set 'out' ports easily whith python

This is on the do what ever you want licence.
"""

# Using the old version of BeautifulSoup (version 3.x)
from BeautifulSoup import BeautifulSoup
import urllib2
from os import name # , system

"""
TODO: 	1. Add PING (icmp)
        2. Add SetPort function.
        3. Rewrite in Python 3
        4. Use the new BeautifulSoup instead
"""


def getsoup(IPIO_addr="192.168.1.100"):
  htmlsoup = urllib2.urlopen("http://"+IPIO_addr+"/ipio.cgi").read()
  soup = BeautifulSoup(htmlsoup)
  return soup


def filterports(IPIO_addr="192.168.1.100", ptype='in', soup=0):
    if soup != 0:
        pfiltered = soup.findAll('input', type="checkbox")
        return pfiltered
    else
        soup = getsoup(IPIO_addr)
        return pfiltered


def getport(IPIO_addr="192.168.1.100", ptype='in', pfiltered=0):
    if pfiltered != 0:
    pnr = 0 # pnr = 0 # define portnr. -> in ports 1-8
    if ptype == 'out':
      pnr = 8 # if ptype == out: portnr. = 8 -> out ports 9-16
    # search soup for porttype
    rlist = [] # Returnlistemty list add items with: inpstate.append()
    for pnr in range(16):
      # find lines containing activ ports
      pstate = 'checked' in str(pfiltered[pnr]) # find lines containing 'checked'
      rlist.append(pstate) # append port state to output list
      if ptype == 'in' and pnr == 8:
        return rlist # return the list
      if ptype == 'out' and pnr == 16:
          return rlist


def setport(IPIO_addr="192.168.1.100", NewPortstate[], pfiltered=0):
    # read the previous port states
    portstate = getport(pfiltered, 'out')
    # set new port states plus the unchanched once
    for pnr in range(8):
        if NwePortstate[pnr] == 'on':
            portstate[pnr] == 'on'
    # requelsting the API URL to set all ports
    requeststring = "?port1=",setport[0],"&port2=",setport[1],"&port3=",setport[2],"&port4=",setport[3],"&port5=",setport[4],"&port6=",setport[5],"&port7=",setport[6],"&port8=",setport[7]
    response = urllib2.urlopen("http://"+IPIO_addr+"/ipio.cgi").read()

