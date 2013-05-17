"""
    shellapi.py
    
    Created by: Philipp Mayr at 10. 05. 13 (Germany)
    
    Lisense: 
    
    This pogram provides the state of the Ports form the "ELV IPIO 88".
    The output comes to stdout
    
    TODO: Add setport function trough stdin
    
    --- USAGE ---
    
    output description:
        1. Line -> IP-Address of the device wich is used
        2. Line -> The states of the IN-Ports (0 is off and 1 is on)
        3. Line -> The states of the OUT-Ports (0 is off and 1 is on)
        
        INFO: If the Values of the portstates are delivered inn HEX you have to back convert them to binary to get a single portstate.
    
    example output (BIN):
        192.168.0.99"
        10100011
        11101101
    
    example output (HEX):
        192.168.0.99
        0xa3ed
    
    errors thrown on stderr:
        NoRouteToHost
        InvalidShellArgs
        IPNotGiven

"""

import sys
import core.elvipio88 as io

devaddr = 'IPNotGiven'

# Shell arguments...
if len(sys.argv) > 4:
    # Help Text
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print "Try: python ",sys.argv[0]," --address 'IPAddress' "
        sys.exit()

    # IP Address 
    if sys.argv[1] == "--address" or sys.argv[1] == "-a":
        devaddr = sys.argv[2]

    # Output Format BIN or HEX
    if sys.argv[3] == "-out" or sys.argv[3] == "-o":
        if sys.argv[4] == "HEX":
            OutputFormat = "HEX"
        elif sys.argv[4] == "BIN":
            OutputFormat = "BIN"
else:
    print >> sys.stderr, "InvalidShellArgs"
    sys.exit(1)

if devaddr != 'IPNotGiven':
    print devaddr # Print The IP-Address of the Device in specified in the First line
else:
    print >> sys.stderr, 'IPNotGiven'
    sys.exit(1)

try:
    soup = io.getsoup(devaddr)
except:
    print >> sys.stderr, "NoRouteToHost" # If there is no route then throw an error
    sys.exit(1)

pfiltered = io.filterports(soup) # filtering lines containing portstate


if OutputFormat == "BIN":
    InPortState = io.getport(devaddr, pfiltered, ptype='in') # Get the 8 IN-Port states in BIN format
    OutPortState =  io.getport(devaddr, pfiltered, ptype='out') # Get the 8 OUT-Port states in BIN format

    print InPortState
    print OutPortState

elif OutputFormat == "HEX":
    PortsHEX = io.getportHEX(devaddr, pfiltered) # Get the HEX values of all ports
    print PortsHEX # and print them
