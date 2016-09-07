import os
import time

led0_on  = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr0/brightness'
led0_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr0/brightness'
led1_on  = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr1/brightness'
led1_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr1/brightness'
led2_on  = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr2/brightness'
led2_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr2/brightness'
led3_on  = 'echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness'
led3_off = 'echo 0 > /sys/class/leds/beaglebone\:green\:usr3/brightness'

i = 0

while True:
 if i == 0:
  os.system(led0_off)
  os.system(led1_off)
  os.system(led2_off)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 1:
  os.system(led0_on)
  os.system(led1_off)
  os.system(led2_off)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 2:
  os.system(led0_off)
  os.system(led1_on)
  os.system(led2_off)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 3:
  os.system(led0_on)
  os.system(led1_on)
  os.system(led2_off)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 4:
  os.system(led0_off)
  os.system(led1_off)
  os.system(led2_on)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 5:
  os.system(led0_on)
  os.system(led1_off)
  os.system(led2_on)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 6:
  os.system(led0_off)
  os.system(led1_on)
  os.system(led2_on)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 7:
  os.system(led0_on)
  os.system(led1_on)
  os.system(led2_on)
  os.system(led3_off)
  i += 1
  time.sleep(1)

 elif i == 8:
  os.system(led0_off)
  os.system(led1_off)
  os.system(led2_off)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 9:
  os.system(led0_on)
  os.system(led1_off)
  os.system(led2_off)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 10:
  os.system(led0_off)
  os.system(led1_on)
  os.system(led2_off)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 11:
  os.system(led0_on)
  os.system(led1_on)
  os.system(led2_off)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 12:
  os.system(led0_off)
  os.system(led1_off)
  os.system(led2_on)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 13:
  os.system(led0_on)
  os.system(led1_off)
  os.system(led2_on)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 14:
  os.system(led0_off)
  os.system(led1_on)
  os.system(led2_on)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 15:
  os.system(led0_on)
  os.system(led1_on)
  os.system(led2_on)
  os.system(led3_on)
  i += 1
  time.sleep(1)

 elif i == 16:
  i = 1
