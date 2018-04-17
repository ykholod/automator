###
#   April 12, 2018
#   Copyright Yaroslav Kholod
#   Author Yaroslav Kholod
 
#   Description:
#   Load WeatherStation files to ESP8266 board

#   Runs automaticaly from automator.py script


#usr/bin/python

import os
import time

os.chdir('/home/vagrant/weather-station')
for file in os.listdir('.'):
    if file.endswith('.py'):
        print 'Uploading ' + file
        os.system('ampy -p /dev/ttyUSB0 -b 115200 put ' + file + ' /'+ file)
os.system('ampy -p /dev/ttyUSB0 -b 115200 reset')
