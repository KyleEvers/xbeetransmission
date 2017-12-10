#!/usr/bin/env python
from xbeetransmission import xbeesend
import serial
import os
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=.5)


f = open("xbee.png", 'rb')
data = f.read() # read the entire content of the file
f.close()

xbeesend(data, ser, "hello")
