import os
import sys
import time

os.system('airmon-ng start wlan2') #needs to be changed depending on the wifi adapter
os.system('airmon-ng check kill')
os.system('airodump-ng wlan2mon')  #needs to be changed as well
 

