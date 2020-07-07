#auto_report_30003, report joint torque in 100 HZ
import socket
import struct
import sys
savedStdout = sys.stdout
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# from matplotlib import pyplot as plt


def bytes_to_fp32(bytes_data, is_big_endian=False):
    """
    bytes to float
    :param bytes_data: bytes
    :param is_big_endian: is big endian or not，default is False.
    :return: fp32
    """
    return struct.unpack('>f' if is_big_endian else '<f', bytes_data)[0]


def bytes_to_fp32_list(bytes_data, n=0, is_big_endian=False):
    """
    bytes to float list
    :param bytes_data: bytes
    :param n: quantity of parameters need to be converted，default is 0，all bytes converted.
    :param is_big_endian: is big endian or not，default is False.
    :return: float list
    """
    ret = []
    count = n if n > 0 else len(bytes_data) // 4
    for i in range(count):
        ret.append(bytes_to_fp32(bytes_data[i * 4: i * 4 + 4], is_big_endian))
    return ret


def bytes_to_u32(data):
    data_u32 = data[0] << 24 | data[1] << 16 | data[2] << 8 | data[3]
    return data_u32

robot_ip = '192.168.1.201'  # IP of controller
robot_port = 30003  # Port of controller

# create socket to connect controller
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(True)
sock.settimeout(1)
sock.connect((robot_ip, robot_port))

for i in range(100):
    data = sock.recv(4)
    length = bytes_to_u32(data)
    data += sock.recv(length - 4)
    j1 = bytes_to_fp32_list(data[59:63])
    j2 = bytes_to_fp32_list(data[63:67])
    j3 = bytes_to_fp32_list(data[67:71])
    j4 = bytes_to_fp32_list(data[71:75])
    j5 = bytes_to_fp32_list(data[75:79])
    j6 = bytes_to_fp32_list(data[79:83])
    # print(j1,j2,j3,j4,j5,j6)
    obj1 = pd.Series(i,j1)

    print(obj1)

