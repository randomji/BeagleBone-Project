#Requires ethernet connection in order to function

import os

os.system('service ntp stop')
os.system('ntpdate sg.pool.ntp.org')
