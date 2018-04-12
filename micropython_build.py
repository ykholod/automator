###
#   April 4, 2018
#   Copyright Yaroslav Kholod
#   Author Yaroslav Kholod
 
#   Description:
#   Build MicroPython with ESP8266 SDK

#   Runs automaticaly from automator.py script


#usr/bin/python

import os
from shutil import copyfile

CC_PATH = 'xtensa-lx106-elf'
print 'Building ESP open SDK'
os.chdir('/home/vagrant/esp-open-sdk')
os.system('make STANDALONE=y')
path = os.environ['PATH']
if CC_PATH not in path:
    os.system('export PATH=/home/vagrant/esp-open-sdk/xtensa-lx106-elf/bin:$PATH')
    os.system('echo "PATH=$(pwd)/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile')

print 'Building MicroPython image'
os.chdir('/home/vagrant/micropython')
os.system('make -C mpy-cross')
os.chdir('/home/vagrant/micropython/ports/esp8266')
os.system('make axtls')
os.system('make')
if (os.path.exists('./build/firmware-combined.bin')):
    copyfile('./build/firmware-combined.bin', '/vagrant/firmware-combined.bin')
    print 'Success: /vagrant/firmware-combined.bin image built'
else:
    print 'Fail to build MicroPython image with ESP open SDK\n'
    print 'Try to reboot VM and build again.'
