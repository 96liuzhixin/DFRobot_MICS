# -*- coding:utf-8 -*-
""" 
  @file get_gas_ppm.py
  @brief Read gas concentration unit(PPM).
  @n step: we must first determine the i2c device address, will dial the code switch A0, A1 (ADDRESS_0 for [0 0]), (ADDRESS_1 for [1 0]), (ADDRESS_2 for [0 1]), (ADDRESS_3 for [1 1]).
  @n       Then wait for the calibration to succeed.
  @n       The calibration time is approximately three minutes.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.1
  date  2021-04-20
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_MicsSensor
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from DFRobot_MICS import *

CALIBRATION_TIME = 0x03            # calibration time
I2C_BUS          = 0x01            # default use I2C1
'''
   # The first  parameter is to select i2c0 or i2c1
   # The second parameter is the i2c device address
   # The default address for i2c is ADDRESS_3
   # ADDRESS_0                 = 0x75
   # ADDRESS_1                 = 0x76
   # ADDRESS_2                 = 0x77
   # ADDRESS_3                 = 0x78
'''
mics = DFRobot_MICS_I2C (I2C_BUS ,ADDRESS_3)

def setup():
  '''
    # Gets the power mode of the sensor
    # The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    # The data obtained in sleep mode is wrong
  '''
  if mics.get_power_mode() == SLEEP_MODE:
    mics.wakeup_mode()
    print "wake up sensor success"
  else:
    print "the sensor is wake up mode"

  '''
    # Do not touch the sensor probe when preheating the sensor.
    # Place the sensor in clean air.
    # The default calibration time is 3 minutes.
  '''
  mics.warm_up_time(CALIBRATION_TIME)

def loop():
  '''
    # Type of detection gas
      # CO       = 0x01  (Carbon Monoxide)
      # CH4      = 0x02  (Methane)
      # C2H5OH   = 0x03  (Ethanol)
      # H2       = 0x06  (Hydrogen)
      # NH3      = 0x08  (Ammonia)
      # NO2      = 0x0A  (Nitrogen Dioxide)
  '''
  gas_concentration = mics.get_gas_ppm(CO)
  print "gas concentration is %.1f"%gas_concentration
  time.sleep(1)
  #mics.sleep_mode()

if __name__ == "__main__":
  setup()
  while True:
    loop()