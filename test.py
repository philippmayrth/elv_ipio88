import elvipio88 as io
from BeautifulSoup import BeautifulSoup
import time


print "\n [i] ",time.ctime() # print the time

devaddr = "ipio8817050.fritz.box"
print " [i] using the address: '",devaddr,"' for the IO\n"

soup = io.getsoup(devaddr)
print " [i] got soup\n"

pfiltered = io.filterports(soup)
print " [i] filtered lines containing port state"
print "\n\n"

print " [i] State of INports 1-8:\n"
print str(io.getport(pfiltered, ptype='in'))+"\n"

print " [i] State of OUTports 1-8:\n"
print str(io.getport(pfiltered, ptype='out'))+"\n"


print "\n [i] ",time.ctime() # print the time