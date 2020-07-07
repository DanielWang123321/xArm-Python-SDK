#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2020, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
# Notice
#   1. Changes to this file on Studio will not be preserved
#   2. The next conversion will overwrite the file with the same name
"""
import sys
import time
import datetime
import threading

"""
# xArm-Python-SDK: https://github.com/xArm-Developer/xArm-Python-SDK
# git clone git@github.com:xArm-Developer/xArm-Python-SDK.git
# cd xArm-Python-SDK
# python setup.py install
"""
from xarm import version
from xarm.wrapper import XArmAPI
from xarm.core.utils.log import logger

logger.setLevel(logger.VERBOSE)

print('xArm-Python-SDK Version:{}'.format(version.__version__))

arm = XArmAPI('192.168.1.15',timed_comm=False)
arm.clean_warn()
arm.clean_error()
arm.motion_enable(True)
arm.set_mode(0)
arm.set_state(0)
time.sleep(1)

params = {'speed': 100, 'acc': 2000, 'angle_speed': 20, 'angle_acc': 500, 'events': {}, 'variables': {}, 'quit': False}


# Register error/warn changed callback
def error_warn_change_callback(data):
    if data and data['error_code'] != 0:
        arm.set_state(4)
        params['quit'] = True
        print('err={}, quit'.format(data['error_code']))
        arm.release_error_warn_changed_callback(error_warn_change_callback)
arm.register_error_warn_changed_callback(error_warn_change_callback)


# Register state changed callback
def state_changed_callback(data):
    if data and data['state'] == 4:
        if arm.version_number[0] >= 1 and arm.version_number[1] >= 1 and arm.version_number[2] > 0:
            params['quit'] = True
            print('state=4, quit')
            arm.release_state_changed_callback(state_changed_callback)
arm.register_state_changed_callback(state_changed_callback)


# Register counter value changed callback
if hasattr(arm, 'register_count_changed_callback'):
    def count_changed_callback(data):
        print('counter val: {}'.format(data['count']))
    arm.register_count_changed_callback(count_changed_callback)

arm.set_counter_reset()
if 'counter' in locals():
    counter = 0
else:
    params['variables']['counter'] = 0
for i in range(int(1000000)):
    if params['quit']:
        break
    arm.set_counter_increase()
    params['speed'] = 200
    params['acc'] = 7734
    params['angle_acc'] = 129
    # if not params['quit']:
    #     arm.set_tcp_load(0.61, [0, 0, 53])
    #     arm.set_state(0)
    # if not params['quit']:
    #     arm.set_tcp_load(0, [0, 0, 0])
    #     arm.set_state(0)
    # if not params['quit']:
    #     arm.set_tcp_load(0.82, [0, 0, 48])
    #     arm.set_state(0)
    # if not params['quit']:
    #     arm.set_tcp_load(5, [0, 0, 0])
    #     arm.set_state(0)
    # if not params['quit']:
    #     code = arm.set_cgpio_digital(0, 0, delay_sec=0)
    #     if code != 0:
    #         print('set_cgpio_digital0, code={}'.format(code))
    #         params['quit'] = True
    # if not params['quit']:
    #     code = arm.set_cgpio_digital(0, 1, delay_sec=0)
    #     if code != 0:
    #         print('set_cgpio_digital1, code={}'.format(code))
    #         params['quit'] = True
    # if not params['quit']:
    #     code = arm.set_cgpio_analog(0, 0)
    #     if code != 0:
    #         print('arm.set_cgpio_analog0, code={}'.format(code))
    #         params['quit'] = True
    # if not params['quit']:
    #     code = arm.set_cgpio_analog(0, 5)
    #     if code != 0:
    #         print('arm.set_cgpio_analog5, code={}'.format(code))
    #         params['quit'] = True
    if not params['quit']:
        code = arm.set_tgpio_digital(0, 0, delay_sec=0)
        if code != 0:
            print('set_tgpio_digital0, code={}'.format(code))
            params['quit'] = True
    if not params['quit']:
        code = arm.set_tgpio_digital(0, 1, delay_sec=0)
        if code != 0:
            print('set_tgpio_digital1, code={}'.format(code))
            params['quit'] = True
    params['angle_acc'] = 129
    if 'counter' in locals():
        counter += 1
    else:
        params['variables']['counter'] += 1
    print('{}'.format((params['variables'].get('counter', 0) if 'counter' not in locals() else counter)))
    # if not params['quit']:
    #     arm.set_suction_cup(True, wait=False, delay_sec=0)
    # if not params['quit']:
    #     arm.set_suction_cup(False, wait=False, delay_sec=0)
arm.release_error_warn_changed_callback(state_changed_callback)
arm.release_state_changed_callback(state_changed_callback)
if hasattr(arm, 'release_count_changed_callback'):
    arm.release_count_changed_callback(count_changed_callback)
