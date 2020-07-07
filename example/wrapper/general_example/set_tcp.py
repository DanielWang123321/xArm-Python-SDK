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
offset1=[100,0,0,0,0,0]
offset2=[150,0,0,0,0,0]

arm.set_position(207,0,112,180,0,0,wait=True,is_radian=False)
arm.set_tcp_offset(offset=offset1)
arm.save_conf()
time.sleep(1)
print(arm.get_position())
arm.set_tcp_offset(offset=offset2)
arm.save_conf()
print(arm.get_position())
