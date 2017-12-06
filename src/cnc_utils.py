#!/usr/bin/python
import serial
import time
import numpy as np

class CNC(object): 
   def __init__(self,port="/dev/ttyUSB0",homing=False):
      self.port=port
      self.s = serial.Serial(self.port,115200)
      self.s.write("\r\n\r\n")
      time.sleep(2)
      self.s.flushInput()

      if homing: home(self.s)
      self.s.write("G90 \n")
      grbl_out=self.s.readline()
      print ' : ' + grbl_out.strip()
      self.s.write("G21 \n")
      grbl_out=self.s.readline()
      print ' : ' + grbl_out.strip()
   
   def home(self):
      send_cmd("$H \n",self.s)
      #send_cmd("g28 \n",s)
      send_cmd("g92 x0 y0 z0 \n",self.s)

   def send_cmd(self,cmd):
       print cmd
       self.s.write(cmd)
       grbl_out=self.s.readline()
       print ' : ' + grbl_out.strip()
       return grbl_out


def clamped(value, minval, maxval, scale):
   return int(scale*np.clip(float(value), minval, maxval))