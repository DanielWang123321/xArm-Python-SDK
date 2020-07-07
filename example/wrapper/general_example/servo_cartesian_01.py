#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>


"""
Description: Servo cartesian
"""
import os
import sys
import time
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from xarm.wrapper import XArmAPI


arm = XArmAPI('192.168.1.201')
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

#set start point by joint motion
# arm.set_position(*[200, 0, 200, 180, 0, 0], wait=True)
arm.set_servo_angle(angle=[0,-42.6,3.2,0,39.4,0],speed=60,wait=True)
print(arm.get_position())

arm.set_mode(1)
arm.set_state(0)
time.sleep(0.1)

while arm.connected and arm.state != 4:
    for i in range(300):
        x = 200 + i
        arm.set_servo_cartesian([x, 0, 200, 180, 0, 0])
        mvpose = [x, 0, 200, 180, 0, 0]
        ret = arm.set_servo_cartesian(mvpose)
        print('set_servo_cartesian, ret={}'.format(ret))
        time.sleep(0.005)
    for i in range(300):
        x = 500 - i
        arm.set_servo_cartesian([x, 0, 200, 180, 0, 0])
        mvpose = [x, 0, 200, 180, 0, 0]
        ret = arm.set_servo_cartesian(mvpose)
        print('set_servo_cartesian, ret={}'.format(ret))
        time.sleep(0.005)

arm.disconnect()
