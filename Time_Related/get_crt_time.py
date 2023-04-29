from datetime import datetime
# This script is used to obtain real-time timestamps, which will be recorded 
# by the researcher into a specified text file.

dt = datetime.now()
dt = datetime.strftime(dt, "%Y-%m-%d %H:%M:%S.%f")
print(dt[:-3])
