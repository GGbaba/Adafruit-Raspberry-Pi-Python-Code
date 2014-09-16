#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import call
import subprocess

def run_cmd(cmd): 
   p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
   output = p.communicate()[0] 
   return output
   
# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.backlight(1)
lcd.clear()
#lcd.message("Adafruit RGB LCD\nPlate w/Keypad!")
sleep(1)
lcd.backlight(0)

# Cycle through backlight colors
#col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
#       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
#for c in col:
#    lcd.backlight(c)
#    sleep(.5)

# Poll buttons, display message & set backlight accordingly
btn = ((lcd.SELECT, 'mpc'                       , lcd.ON),
       (lcd.RIGHT , 'shairport'                 , lcd.RED),
       (lcd.UP    , 'etherwake'                 , lcd.BLUE),
       (lcd.DOWN  , 'backlight'                 , lcd.GREEN),
       (lcd.LEFT  , 'resteps'                   , lcd.VIOLET))
       
prev = -1
a=0
c=0
while True:
    sleep(.2)
    for b in btn:
        #sleep(.5) 
        if lcd.buttonPressed(b[0]):
               lcd.clear()
               #if lcd.message(b[1]) == "mpc":
               if b[0] == 0 :
                     if a is 0 :
                            #call(["mpcgg", "play"])
                            #lcd.message("mpc !!!")
                            lcd.message(run_cmd("mpcgg play"))
                            print'Mpc On !!!'
                            a=1
                     else :
                            #call(["mpcgg", "stop"])
                            #lcd.message("mpc !!!")
                            lcd.message(run_cmd("mpcgg stop"))
                            print'Mpc Off'
                            a=0
               #if lcd.message(b[1]) is 'shairport':
               if b[0] == 1 :
                     call(["shairport", "-d"])
                     lcd.message("shairport !!!")
                     print'shairport !!!'
               if b[0] == 2 :
                     if c is 0 : 
                            lcd.message("BackLight ON !")
                            lcd.backlight(1)
                            c=1
                     else :
                            lcd.message("BackLight OFF !")
                            lcd.backlight(0)
                            c=0
               if b[0] == 3 :
                     run_cmd("etherwake 00:24:1d:d1:e0:e3")
                     lcd.message("etherwake to :\n 00:24:1d:d1:e0:e3")
               if b[0] == 4 :
                     run_cmd("sudo pkill mpc && sudo pkill mpcgg && sudo pkill shairport")
                     lcd.message("No Sound !!!")
               #sleep(.2)
               break
               '''
            if b is not prev:
                call(["mpcgg", "play"])
                call(["ls", "-l"])
                lcd.clear()
                lcd.message(b[1])
                #lcd.backlight(b[2])
                prev = b
            break
            '''
