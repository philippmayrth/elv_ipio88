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

# IPIO_addr = "ipio8817050.fritz.box"

"""
TODO: 	1. [ ] Add PING (icmp)
        2. [ ] Add SetPort function.
"""


# get the soup from the IPIO
def getsoup(IPIO_addr):
  if IPIO_addr == '':
    return 0 # 0 = error
  # request the URL, and read the response
  htmlsoup = urllib2.urlopen("http://"+IPIO_addr+"/ipio.cgi").read()
  soup = BeautifulSoup(htmlsoup)
  return soup


# filter the soup for the lines whth the information of the ports
def filterports(soup=0, ptype='in'):
  if soup == 0:
    return 0 # 0 = error
  # find all <input> tags with the type: 'checkbox'
  pfiltered = soup.findAll('input', type="checkbox")
  # convert oupputset to string
  return pfiltered


def gps(pfiltered=0, ptype='in'): # 'in' or 'out'
  # check for errors in the filtered soup
  if pfiltered != 0:
    pnr = 0 # pnr = 0 # define portnr. -> in ports 1-8
    if ptype == 'out':
      pnr = 8 # if ptype == out: portnr. = 8 -> out ports 9-16
    # search soup for porttype
    rlist = [] # Returnlistemty list add items with: inpstate.append()
    while 1:
      # find lines containing activ ports
      pstate = 'checked' in str(pfiltered[pnr]) # find lines containing 'chekced'
      rlist.append(pstate) # append port state to output list
      pnr += 1
      if ptype == 'in' and pnr == 8:
	return rlist # return the list
	break # no more ports to scan
      if ptype == 'out' and pnr == 16:
	return rlist
	break


#def setport():
#  break