import os
import time

os.system('clear')
os.system('figlet -f small Ddos Unistalling | lolcat')
print('[+] System Unistalling... ')
time.sleep(6)
os.system('cd $PREFIX/share && rm -rf DDos-Attack')
print('Almoat Done Wait 3sec..')
os.system('cd $PREFIX/bin && rm ddos')
os.system('cd $PREFIX/bin && rm unistall-ddos')
time.sleep(5)
print('Success Done!')
