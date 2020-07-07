#auto_report_30003, report joint torque in 100 HZ
import socket
import struct
import sys
savedStdout = sys.stdout
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# from matplotlib import pyplot as plt
for i in range(100):
    obj = pd.Series(i)
    print(obj)