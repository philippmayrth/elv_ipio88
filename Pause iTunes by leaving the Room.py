# -*- coding: iso-8859-1 -*-
"""
Autor: Philipp Mayr
Date: 26. 11. 2012
Note: When teh door is opended then pause iTunes. When closed again play.

"""

import sys, os, time
import core.elvipio88 as io

# iTunes Ctrl
iTunesState = "osascript -e \'tell application \"iTunes\" to player state as string\'"
iTunesPlay = "osascript -e \'tell application \"iTunes\" to play\'"
iTunesPause = "osascript -e \'tell application \"iTunes\" to pause\'"
# - iTunes Ctrl

# Output Marukup - TODO: Add support for HTML
OMUWarnign = " \033[1;31m[\033[5;31m!\033[m\033[1;31m] " # red
OMUInfo = "\033[0;34m [i] "
OMUProgram = "\033[0;32m [-] "
OMUFriendly = "\033[0;35m"
OMUEndSig = "\033[m"
# - Terminal Formating

devaddr = "192.168.1.100"

# Get and Process the Soup
def ProcessSoup():
    try:
        soup = io.getsoup(devaddr)
    except:
        print >> sys.stderr, OMUWarnign,"no rout to host\033[0;31m - ",time.ctime(),OMUEndSig
        return "error"
    print OMUInfo,"got soup",OMUEndSig
    
    pfiltered = io.filterports(soup)
    print OMUInfo,"filtered lines containing port state",OMUEndSig
    
    
    print  OMUInfo,"got State of INports 1-8",OMUEndSig
    in_portstate = io.gps(pfiltered, ptype='in')
    return in_portstate


def iTunesControll(in_portstate):
    # Controll iTunes
    # array index 0 (for port 1)
    print OMUProgram,"port 1 is active - ",in_portstate[0]
    
    if in_portstate[0] == True: # port 1
        print OMUProgram,"Play iTunes"
        os.system(iTunesPlay)
    
    else:
        print OMUProgram,"Pause iTunes"
        os.system(iTunesPause)
    
    time.sleep(2) # system entlasten # ipio packt 120ms
    print


def main():
    print OMUInfo,"Started at ",time.ctime(),OMUEndSig
    print OMUInfo,"using the address: ",devaddr," for the IO",OMUEndSig

    try:
        while 1: # endlosschleife
            in_portstate = ProcessSoup()
            if in_portstate != "error":
                iTunesControll(in_portstate)
            else:
                time.sleep(30) # system entlasten (30 sek) pause bevor reconnect.
    except KeyboardInterrupt:
        print OMUInfo,"Ended at ",time.ctime(),OMUEndSig
        print OMUFriendly,"     iyi günler!",OMUEndSig



if __name__ == "__main__":
    main() # init Program

