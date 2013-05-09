import sys
import core.elvipio88 as io

if len(sys.argv) > 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print "Try: python ",sys.argv[0]," --address 'IPAddress'"
        sys.exit()
    if sys.argv[1] == "--address":
        devaddr = sys.argv[2]

print " [i] using the address: ",devaddr," for the IO"

try:
  soup = io.getsoup(devaddr)
except:
  print " [!] no rout to host"
  sys.exit()
print " [i] got soup"

pfiltered = io.filterports(soup)
print " [i] filtered lines containing port state"

print " [i] State of INports 1-8:"
in_portstate = io.getport(pfiltered, ptype='in')

for i in range(8):
    print " [-] port",i+1,"is active - ",in_portstate[i]

print " [i] State of OUTports 1-8:"
out_portstate =  io.getport(pfiltered, ptype='out')

for i in range(8):
    print " [-] port",i+1,"is active - ",out_portstate[i]
