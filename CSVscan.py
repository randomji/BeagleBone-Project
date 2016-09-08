#Scan for MAC addresses only

import os
import time
import sys

def child():
	os.system('airodump-ng wlan2mon -w aircrack-captures/MonitorMode --output-format csv --write-interval 10 --essid xxxxxx')
	os._exit(0)
  
def parent():
	capture = 0
        while(capture < 60):
  	  	capture = capture + 1
    		print("scan : %s"  %capture)
		count = 0
		newpid = os.fork()
		if newpid == 0:
			child()
 		else:
  			while(count < 10):
    				time.sleep(2)
    				count = count + 1
    				print("parent : %s"  %count)
  			os.system('pkill -9 airodump-ng')
  	os.system('pkill -9 python')

parent()  