###
#   April 3, 2018
#   Copyright Yaroslav Kholod
#   Author Yaroslav Kholod
 
#   Description:
#   Load MicroPython image to ESP8266 board

#   Runs automaticaly from automator.py script


#usr/bin/python

import os
import time

print '\nPlease, make sure board is hardwired!\n'
for sec in [5,4,3,2,1]:
    print 'Loading image in ' + str(sec) + ' seconds'
    time.sleep(1)
if (os.path.exists('/vagrant/firmware-combined.bin')):
    print 'Run, Forrest, run'
    os.chdir('/home/vagrant/micropython')
    os.system('/home/vagrant/esptool/esptool.py --port=/dev/ttyUSB0  write_flash  -fm=dio -fs=detect 0x00000 /vagrant/firmware-combined.bin')
else:
    print 'File not present. Please, build MicroPython.'
