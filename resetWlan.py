#Connecting to ethernet

import os
 
os.system('ifdown wlan2')
os.system('ifup wlan2')

