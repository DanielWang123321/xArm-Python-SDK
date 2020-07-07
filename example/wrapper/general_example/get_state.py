import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from xarm.wrapper import XArmAPI


arm = XArmAPI('192.168.1.201')
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
time.sleep(1)
# arm.set_state(4)
while True:
    print(arm.get_state())
    time.sleep(0.1)
