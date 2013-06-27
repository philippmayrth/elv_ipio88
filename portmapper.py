#! /usr/bin/env python
#
# Created by Philipp Mayr on 27. June, 2013 (Germany)
#
# Name: portmapper.py
#
# License: CC NY-NC
#

from core.elvipio88 import elvipio88 as iodevice

if __name__ == "__main__":
    
    io = iodevice()
    state = io.getport()
    
    print ("Ports 0-8 are 'IN' ports and 9-16 are 'OUT' ports")
    
    for port in range(16):
        print ("Port "+str(port)+" state is "+str(state[port]))