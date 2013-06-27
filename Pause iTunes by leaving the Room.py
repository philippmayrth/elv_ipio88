#! /usr/bin/env python
"""
Autor: Philipp Mayr
Date: 26. 11. 2012
Note: When the door is opended then pause iTunes. When closed again play.

"""

import sys, os, time
from core.elvipio88 import elvipio88 as iodevice


class OMU: # Ouptput Markup - Terminal and HTML formating
    Warnign = " \033[1;31m[\033[5;31m!\033[m\033[1;31m] " # red
    Info = "\033[0;34m [i] "
    Program = "\033[0;32m [-] "
    Friendly = "\033[0;35m"
    EndSig = "\033[m"


class iTunes: # iTunes controll Object
    State = "osascript -e \'tell application \"iTunes\" to player state as string\'"
    Play = "osascript -e \'tell application \"iTunes\" to play\'"
    Pause = "osascript -e \'tell application \"iTunes\" to pause\'"
    
    def pause(self):
        os.system(self.Pause)
    
    def play(self):
        os.system(self.Play)



if __name__ == "__main__":
    
    io = iodevice("192.168.1.100")
    iTunes = iTunes()
    
    print OMU.Info,"Started at ",time.ctime(),OMU.EndSig
    print OMU.Info,"using this address: ",io.address," for the IO",OMU.EndSig
    
    try:
        while 1:
            portstate = io.getport()
            
            if portstate[0] == True:
                iTunes.play()
            elif portstate[0] == False:
                iTunes.pause()
            
            time.sleep(30)

    except KeyboardInterrupt:
        print OMU.Info,"Ended at ",time.ctime(),OMU.EndSig
        print OMU.Friendly,"have a nice day!",OMU.EndSig
