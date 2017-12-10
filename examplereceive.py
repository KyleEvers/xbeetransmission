#!/usr/bin/env python
from xbeetransmission import xbeereceive
import serial
import sys
import os

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=.5)

xbeereceive(ser, "hello", "temp.png")
